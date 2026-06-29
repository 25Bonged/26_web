/*
 * Compiles a per-page Tailwind stylesheet for every HTML file, using each
 * page's theme from ./tailwind.themes.cjs (custom colors / fonts) so the static
 * build renders identically to the old cdn.tailwindcss.com runtime.
 *
 * The theme is sourced from tailwind.themes.cjs (NOT from the HTML), so the
 * build stays correct after the inline <script id="tailwind-config"> blocks
 * were removed from the pages.
 *
 * Output: assets/css/<page>.css   (linked from each HTML page)
 * Run:    npm run build:css
 */
const fs = require("fs");
const path = require("path");
const postcss = require("postcss");
const tailwind = require("tailwindcss");
const forms = require("@tailwindcss/forms");
const containerQueries = require("@tailwindcss/container-queries");
const THEMES = require("./tailwind.themes.cjs");

const ROOT = __dirname;
const OUT_DIR = path.join(ROOT, "assets", "css");
fs.mkdirSync(OUT_DIR, { recursive: true });

// 404.html is fully self-contained (inline CSS, no Tailwind) — skip it.
const SKIP = new Set(["404.html"]);

const htmlFiles = fs
  .readdirSync(ROOT)
  .filter((f) => f.endsWith(".html") && !SKIP.has(f));

const INPUT_CSS = "@tailwind base;\n@tailwind components;\n@tailwind utilities;\n";

(async () => {
  let ok = 0;
  const missing = [];
  for (const file of htmlFiles) {
    const base = file.replace(/\.html$/, "");
    const htmlPath = path.join(ROOT, file);
    const theme = THEMES[base];
    if (!theme) missing.push(file); // build continues with Tailwind defaults

    const cfg = theme
      ? JSON.parse(JSON.stringify(theme)) // clone so we don't mutate the shared map
      : { darkMode: "class", theme: { extend: {} } };
    cfg.content = [htmlPath];
    cfg.plugins = [forms, containerQueries];

    const result = await postcss([tailwind(cfg)]).process(INPUT_CSS, {
      from: undefined,
    });
    fs.writeFileSync(path.join(OUT_DIR, base + ".css"), result.css);
    const kb = (result.css.length / 1024).toFixed(1);
    console.log(`  ${file.padEnd(28)} -> assets/css/${base}.css (${kb} KB)`);
    ok++;
  }
  if (missing.length) {
    console.warn(
      `\nWARNING: no theme entry in tailwind.themes.cjs for: ${missing.join(", ")} ` +
        `(compiled with Tailwind defaults — add them if they use custom colors).`
    );
  }
  console.log(`\nCompiled ${ok} stylesheets.`);
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
