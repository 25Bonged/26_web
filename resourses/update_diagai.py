import re

with open('vehicle_lab_vanilla/diagai.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero
hero_old = """                <h1 class="text-6xl md:text-7xl font-black leading-[0.9] tracking-tighter">
                    DiagAI: The <span class="text-[#39ff14]">AI Brain</span> of Vehicle Diagnostics
                </h1>
                <p class="text-xl text-slate-400 leading-relaxed max-w-xl">
                    Transforming raw telemetry into actionable insights with multi-agent orchestration. The industry's
                    first specialized diagnostic reasoning engine for modern automotive engineering.
                </p>"""
hero_new = """                <h1 class="text-6xl md:text-7xl font-black leading-[0.9] tracking-tighter">
                    DiagAI: The <span class="text-[#39ff14]">Senior Engineer</span> in the Machine
                </h1>
                <p class="text-xl text-slate-400 leading-relaxed max-w-xl">
                    A mature, Multi-Agent System for expert diagnostics. Moving beyond simple chat into a coordinated system of specialists, mirroring an entire engineering department.
                </p>"""
html = html.replace(hero_old, hero_new)

# 2. Update Multi-Agent Heading & Plus More box
agent_heading_old = """                <h2 class="flex items-center gap-3 text-3xl md:text-4xl font-black tracking-tighter text-white mb-4">
                    <span class="text-[#39ff14] text-4xl">*</span> The Multi-Agent Ecosystem
                </h2>
                <p class="text-slate-400">Our specialized 8-agent architecture enables deep-dive analysis into every
                    vehicle subsystem. Each agent is trained on petabytes of OEM-specific telemetry data and operates in
                    a collaborative swarm.</p>"""
agent_heading_new = """                <h2 class="flex items-center gap-3 text-3xl md:text-4xl font-black tracking-tighter text-white mb-4">
                    <span class="text-[#39ff14] text-4xl">*</span> The Diagnostic & Calibration Brain
                </h2>
                <p class="text-slate-400">Our specialized architecture features a Diagnostic Brain and a Calibration Brain (scoring 85/100 on engineering maturity), evaluating advanced formulas like BSFC and BMEP natively through a collaborative swarm of expert agents.</p>"""
html = html.replace(agent_heading_old, agent_heading_new)

plus_more_old = """                <div class="text-2xl font-black text-slate-500 mb-2">...</div>
                <div class="text-xs font-bold uppercase tracking-widest text-slate-400">+5 SPECIALIZED AGENTS</div>"""
plus_more_new = """                <div class="text-xl font-black text-[#39ff14] mb-2">DFCAgent, IUPRAgent...</div>
                <div class="text-xs font-bold uppercase tracking-widest text-slate-400">+5 SPECIALIZED AGENTS</div>"""
html = html.replace(plus_more_old, plus_more_new)

# 3. Update Signal Intelligence text
sig_old = """                <p class="text-slate-400 mb-8 text-left">Matching 10,000+ discrete vehicle signals across 785 alias
                    patterns. DiagAI automatically normalizes data from disparate OEM protocols into a unified
                    diagnostic schema.</p>"""
sig_new = """                <div class="flex items-baseline gap-3 mb-2 mt-4">
                    <span class="text-3xl font-black text-white">95/100</span>
                    <span class="text-xs font-bold uppercase tracking-widest text-[#39ff14]">Signal Intelligence Score</span>
                </div>
                <p class="text-slate-400 mb-8 text-left mt-2">Indexing exactly 1,817 active signals and evaluating 155 discrete alias patterns. DiagAI connects generic terms to OEM-specific and ETAS proprietary labels using Exact, Normalized, and Fuzzy partial-word logic.</p>"""
html = html.replace(sig_old, sig_new)

# 4. Insert Validated Performance Section before Dual AI
val_perf = """
    <!-- Validated Performance Section -->
    <div class="max-w-7xl mx-auto px-6 py-24 border-t border-slate-900">
        <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-black text-white tracking-tighter mb-6">Validated Performance:<br/> 100% Success Rate</h2>
            <p class="text-slate-400 max-w-2xl mx-auto">Proven on 20 highly complex engineering queries spanning sophisticated diagnostics, accurate signal correlation, and professional visualizations.</p>
        </div>
        
        <div class="max-w-4xl mx-auto bg-slate-900/40 border border-slate-800 rounded-3xl overflow-hidden shadow-2xl">
            <table class="w-full text-left text-sm text-slate-300">
                <thead class="bg-slate-800/50 text-xs uppercase font-black tracking-widest text-slate-500 border-b border-slate-800">
                    <tr>
                        <th class="px-6 py-4">Metric</th>
                        <th class="px-6 py-4">Result</th>
                        <th class="px-6 py-4 text-right">Status</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-800/50">
                    <tr class="hover:bg-slate-800/20 transition-colors">
                        <td class="px-6 py-4 font-bold text-white">Total Queries Tested</td>
                        <td class="px-6 py-4 font-mono">20</td>
                        <td class="px-6 py-4 text-right text-[#39ff14] text-xl font-black">✓</td>
                    </tr>
                    <tr class="hover:bg-slate-800/20 transition-colors">
                        <td class="px-6 py-4 font-bold text-white">Success Rate / Engineer-Level Responses</td>
                        <td class="px-6 py-4 font-mono font-bold text-[#39ff14]">100% (20/20)</td>
                        <td class="px-6 py-4 text-right">
                             <div class="inline-flex items-center gap-1 text-black text-xs font-bold uppercase tracking-widest bg-[#39ff14] px-2 py-1 rounded">
                                Perfect
                             </div>
                        </td>
                    </tr>
                    <tr class="hover:bg-slate-800/20 transition-colors">
                        <td class="px-6 py-4 font-bold text-white">Visualization Rate</td>
                        <td class="px-6 py-4 font-mono">35% (7/20)</td>
                        <td class="px-6 py-4 text-right text-slate-400">Good</td>
                    </tr>
                </tbody>
            </table>
            <div class="p-6 bg-[#39ff14]/5 border-t border-[#39ff14]/20">
                <p class="text-[#39ff14] font-medium italic text-center">"CONFIRMED: Your DiagAI system demonstrates SENIOR VEHICLE DIAGNOSTICS ENGINEER capabilities."</p>
            </div>
        </div>
    </div>

"""
html = html.replace('    <!-- Dual AI Inference Engine -->', val_perf + '    <!-- Dual AI Inference Engine -->')

with open('vehicle_lab_vanilla/diagai.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated diagai.html")
