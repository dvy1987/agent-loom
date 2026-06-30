#!/usr/bin/env node
// APCA contrast (APCA-W3 0.1.9 constants). Perceptual; accurate on dark themes + thin type.
// Usage:
//   node apca.mjs "#1A1A1A" "#FAFAF7"        -> prints Lc for text=#1A1A1A on bg=#FAFAF7
//   node apca.mjs --check pairs.json          -> [{ "name":"body", "text":"#..", "bg":"#..", "min":75 }]
// Targets: body Lc>=75, large/bold Lc>=45, non-text UI Lc>=30.

const mainTRC = 2.4;
const Rco = 0.2126729, Gco = 0.7151522, Bco = 0.072175;
const normBG = 0.56, normTXT = 0.57, revTXT = 0.62, revBG = 0.65;
const blkThrs = 0.022, blkClmp = 1.414, scale = 1.14;
const loOffset = 0.027, deltaYmin = 0.0005, loClip = 0.1;

function hexToRgb(hex) {
  const h = hex.replace("#", "").trim();
  const full = h.length === 3 ? h.split("").map((c) => c + c).join("") : h;
  if (full.length !== 6 || /[^0-9a-fA-F]/.test(full)) throw new Error(`bad hex: ${hex}`);
  return [0, 2, 4].map((i) => parseInt(full.slice(i, i + 2), 16));
}

function sRGBtoY([r, g, b]) {
  const lin = (v) => Math.pow(v / 255, mainTRC);
  return Rco * lin(r) + Gco * lin(g) + Bco * lin(b);
}

export function apca(textHex, bgHex) {
  let txtY = sRGBtoY(hexToRgb(textHex));
  let bgY = sRGBtoY(hexToRgb(bgHex));
  txtY = txtY > blkThrs ? txtY : txtY + Math.pow(blkThrs - txtY, blkClmp);
  bgY = bgY > blkThrs ? bgY : bgY + Math.pow(blkThrs - bgY, blkClmp);
  if (Math.abs(bgY - txtY) < deltaYmin) return 0;
  let out;
  if (bgY > txtY) {
    const sapc = (Math.pow(bgY, normBG) - Math.pow(txtY, normTXT)) * scale;
    out = sapc < loClip ? 0 : sapc - loOffset;
  } else {
    const sapc = (Math.pow(bgY, revBG) - Math.pow(txtY, revTXT)) * scale;
    out = sapc > -loClip ? 0 : sapc + loOffset;
  }
  return Math.round(out * 100 * 10) / 10;
}

const args = process.argv.slice(2);
if (args[0] === "--check" && args[1]) {
  const fs = await import("node:fs");
  const pairs = JSON.parse(fs.readFileSync(args[1], "utf8"));
  let failed = 0;
  for (const p of pairs) {
    const lc = Math.abs(apca(p.text, p.bg));
    const min = p.min ?? 75;
    const ok = lc >= min;
    if (!ok) failed++;
    console.log(`${ok ? "PASS" : "FAIL"}  Lc ${lc}  (min ${min})  ${p.name ?? ""}  ${p.text} on ${p.bg}`);
  }
  console.log(`\n${failed === 0 ? "All pairs pass." : `${failed} pair(s) FAILED.`}`);
  process.exit(failed === 0 ? 0 : 1);
} else if (args.length >= 2) {
  console.log(`Lc ${apca(args[0], args[1])}  (text ${args[0]} on bg ${args[1]})`);
} else {
  console.log('Usage: node apca.mjs "#text" "#bg"   |   node apca.mjs --check pairs.json');
  process.exit(1);
}
