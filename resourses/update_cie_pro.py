import re

with open('vehicle_lab_vanilla/cie_pro.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero
html = html.replace(
    'The Intelligence Engine for <br />\n          <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500 italic">Model-Based\n            Calibration</span>',
    'The Intelligence Engine for <br />\n          <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500 italic">Next-Generation\n            Calibration</span>'
)

hero_p_old = """<p class="text-xl text-slate-400 leading-relaxed max-w-xl">
          Revolutionize your calibration workflow with industry-leading optimization and physics-informed modeling.
          Reduce test time by 70% while ensuring 100% safety compliance.
        </p>"""
hero_p_new = """<p class="text-xl text-slate-400 leading-relaxed max-w-xl">
          The modern platform to replace your legacy, fragmented toolchain. Eliminate disconnected tools and expensive test cycles. Complete your entire workflow—from data ingest to ECU export—in a single, intelligent, AI-first environment.
        </p>"""
html = html.replace(hero_p_old, hero_p_new)

# 2. Insert Ingest & DoE Sections
new_sections = """  <!-- Data & Modeling Section -->
  <div class="max-w-7xl mx-auto px-6 py-24 border-t border-slate-900">
    <div class="mb-20">
      <div class="text-blue-500 font-black uppercase tracking-[0.3em] text-[11px] mb-4">Ingest & Train</div>
      <h2 class="text-5xl md:text-6xl font-black tracking-tighter text-white">Understand Data & Train Models in Minutes</h2>
      <p class="text-xl text-slate-400 mt-6 max-w-2xl">Skip manual conversion and hyperparameter tuning. Go from raw dyno data to production-grade surrogates instantly.</p>
    </div>

    <div class="grid md:grid-cols-2 gap-8">
      <!-- Ingest Card -->
      <div class="bg-slate-900/40 border border-slate-800 p-10 rounded-[2.5rem] hover:border-blue-500/30 transition-all group">
        <div class="w-14 h-14 bg-blue-500/10 rounded-2xl flex items-center justify-center text-blue-500 mb-8 group-hover:bg-blue-500 group-hover:text-white transition-all">
          <span class="material-symbols-outlined text-3xl">database</span>
        </div>
        <h3 class="text-2xl font-bold mb-4">Multi-Format Ingest & QA</h3>
        <p class="text-slate-400 leading-relaxed mb-6">Drag-and-drop support for CSV, MDF, Excel, MAT, and HDF5. Features automated signal decoding and instant quality assurance, flagging missing values and zero-variance signals before training begins.</p>
      </div>
      <!-- Models Card -->
      <div class="bg-slate-900/40 border border-slate-800 p-10 rounded-[2.5rem] hover:border-cyan-500/30 transition-all group">
        <div class="w-14 h-14 bg-cyan-500/10 rounded-2xl flex items-center justify-center text-cyan-500 mb-8 group-hover:bg-cyan-500 group-hover:text-white transition-all">
          <span class="material-symbols-outlined text-3xl">model_training</span>
        </div>
        <h3 class="text-2xl font-bold mb-4">World-Class Model Suite & AutoML</h3>
        <p class="text-slate-400 leading-relaxed mb-6">Access Random Forest, Gradient Boosting, GP, RBF, and PCE. Optuna-powered AutoML automatically finds the optimal architecture with built-in 5-fold cross-validation ensuring R² > 0.95.</p>
        <div class="flex gap-4">
          <div class="bg-black/60 rounded-xl px-4 py-2 border border-slate-800">
            <div class="text-[10px] uppercase font-bold text-slate-500">R² Score</div>
            <div class="text-lg font-black text-green-400">0.982</div>
          </div>
          <div class="bg-black/60 rounded-xl px-4 py-2 border border-slate-800">
            <div class="text-[10px] uppercase font-bold text-slate-500">RMSE</div>
            <div class="text-lg font-black text-blue-400">2.15</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Smarter DoE Section -->
  <div class="max-w-7xl mx-auto px-6 py-24 border-t border-slate-900">
    <div class="text-center mb-20">
      <div class="text-cyan-500 font-black uppercase tracking-[0.3em] text-[11px] mb-4">Smarter DoE</div>
      <h2 class="text-5xl md:text-6xl font-black text-white tracking-tighter">Slash Dyno Time by 30-50%</h2>
      <p class="text-xl text-slate-400 mt-6 max-w-2xl mx-auto">Generate optimal test plans that automatically adapt to your physical limits.</p>
    </div>
    <div class="grid md:grid-cols-2 gap-8">
      <div class="bg-slate-900/40 border border-slate-800 p-8 rounded-[2rem]">
        <h3 class="text-xl font-bold mb-3 text-white">Comprehensive Static DoE</h3>
        <p class="text-slate-400 text-sm leading-relaxed">Optimal space-filling test plans for steady-state mapping using D-Optimal, Latin Hypercube (LHS), Sobol, and Box-Behnken methods.</p>
      </div>
      <div class="bg-slate-900/40 border border-slate-800 p-8 rounded-[2rem]">
        <h3 class="text-xl font-bold mb-3 text-white">Dynamic DoE for Transients</h3>
        <p class="text-slate-400 text-sm leading-relaxed">Time-based sequences with sinusoidal frequency sweeps. Automatically obeys safety limits and convex hull constraints to stay within valid envelopes.</p>
      </div>
    </div>
  </div>

  <!-- Optimization Suite Section -->"""
html = html.replace('  <!-- Optimization Suite Section -->', new_sections)

# 3. Update Optimization Headers
opt_old = """    <div class="mb-20">
      <div class="text-blue-500 font-black uppercase tracking-[0.3em] text-[11px] mb-4">Optimization Suite</div>
      <h2 class="text-6xl font-black tracking-tighter text-white">Algorithms for Peak Performance</h2>
      <p class="text-xl text-slate-400 mt-6 max-w-2xl">Navigate complex design spaces with automated constraint
        handling.</p>
    </div>"""
opt_new = """    <div class="mb-20">
      <div class="text-blue-500 font-black uppercase tracking-[0.3em] text-[11px] mb-4">Optimization Suite</div>
      <h2 class="text-6xl font-black tracking-tighter text-white">Interactive Pareto Fronts</h2>
      <p class="text-xl text-slate-400 mt-6 max-w-2xl">Solve complex multi-objective problems. Achieve 50-70% faster convergence to the optimal solution using state-of-the-art constraint-aware optimizers.</p>
    </div>"""
html = html.replace(opt_old, opt_new)

# 4. Update Map Generation
map_old = """      <h2 class="text-6xl font-black text-white">Automated 2D/3D Map Generation</h2>
      <p class="text-xl text-slate-400 mt-6 max-w-2xl mx-auto">Generates production-ready calibration maps with in-loop
        data-quality constraints. Never skip the automation loop.</p>"""
map_new = """      <h2 class="text-5xl md:text-6xl font-black text-white tracking-tighter">Generate & Export Production Calibrations</h2>
      <p class="text-xl text-slate-400 mt-6 max-w-2xl mx-auto">Create 2D/3D maps with interactive validation, physical constraints (smoothing, monotonicity), and seamless export to ETAS INCA, AVL CAMEO, and ASAM formats (A2L, CDF, HEX).</p>"""
html = html.replace(map_old, map_new)

with open('vehicle_lab_vanilla/cie_pro.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated cie_pro.html")
