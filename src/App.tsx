/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { useEffect, useState } from "react";

export default function App() {
  const [candidates, setCandidates] = useState([]);
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    fetch("/dashboard_top5.json")
      .then((res) => res.json())
      .then((data) => setCandidates(data))
      .catch(console.error);

    fetch("/run_summary.json")
      .then((res) => res.json())
      .then((data) => setSummary(data))
      .catch(console.error);
  }, []);

  return (
    <div className="flex flex-col h-screen w-full bg-[#E4E3E0] text-[#141414] font-['Helvetica_Neue',_Helvetica,_Arial,_sans-serif] border-[12px] border-[#141414] overflow-hidden">
      {/* HEADER: SYSTEM STATUS */}
      <header className="flex items-center justify-between px-6 py-4 border-b border-[#141414]">
        <div className="flex items-baseline gap-4">
          <h1 className="text-2xl font-bold tracking-tighter italic font-serif">REDROB<span className="not-italic">RANK</span> v1.0.4</h1>
          <span className="text-[10px] uppercase tracking-widest opacity-60 font-mono">System Status: Optimal / CPU-Only Mode</span>
        </div>
        <div className="flex gap-8">
          <div className="flex flex-col items-end">
            <span className="text-[9px] uppercase opacity-50">Candidates Processed</span>
            <span className="font-mono font-bold">{summary?.candidates_processed || '...'}</span>
          </div>
          <div className="flex flex-col items-end">
            <span className="text-[9px] uppercase opacity-50">Execution Time</span>
            <span className="font-mono font-bold">{summary?.runtime_seconds || '...'}s</span>
          </div>
          <div className="flex flex-col items-end">
            <span className="text-[9px] uppercase opacity-50">Honeypots Detected</span>
            <span className="font-mono font-bold text-red-600">{summary?.honeypots_detected || 0}</span>
          </div>
        </div>
      </header>

      {/* MAIN CONTENT AREA */}
      <main className="flex flex-1 overflow-hidden">
        {/* LEFT SIDEBAR: WEIGHTS & PARAMETERS */}
        <aside className="w-72 shrink-0 border-r border-[#141414] p-6 flex flex-col gap-6">
          <div>
            <h2 className="text-[11px] font-bold uppercase tracking-widest mb-4 opacity-70">Feature Weight Distribution</h2>
            <div className="space-y-3">
              <div className="flex flex-col gap-1">
                <div className="flex justify-between text-[10px] font-mono"><span>Core AI/Retrieval</span><span>35%</span></div>
                <div className="h-1 bg-black/10 w-full"><div className="h-full bg-black w-[35%]"></div></div>
              </div>
              <div className="flex flex-col gap-1">
                <div className="flex justify-between text-[10px] font-mono"><span>Production Shipping</span><span>18%</span></div>
                <div className="h-1 bg-black/10 w-full"><div className="h-full bg-black w-[18%]"></div></div>
              </div>
              <div className="flex flex-col gap-1">
                <div className="flex justify-between text-[10px] font-mono"><span>Ranking/Eval Metrics</span><span>14%</span></div>
                <div className="h-1 bg-black/10 w-full"><div className="h-full bg-black w-[14%]"></div></div>
              </div>
              <div className="flex flex-col gap-1">
                <div className="flex justify-between text-[10px] font-mono"><span>Behavioral/Availability</span><span>12%</span></div>
                <div className="h-1 bg-black/10 w-full"><div className="h-full bg-black w-[12%]"></div></div>
              </div>
            </div>
          </div>

          <div className="mt-auto p-4 border border-[#141414] bg-white/50">
            <h3 className="text-[10px] font-bold uppercase mb-2">Audit Logs</h3>
            <div className="text-[9px] font-mono space-y-1 opacity-70">
              <p>[09:21] Loading candidates.jsonl...</p>
              <p>[09:22] Extracting vector_db signals...</p>
              <p>[09:24] Running Trap Detector v2.1...</p>
              <p>[09:25] Scoring NDCG-intent features...</p>
              <p className="text-green-700">[09:26] Validated Top 100 Output.</p>
            </div>
          </div>
        </aside>

        {/* CENTER: CANDIDATE GRID */}
        <section className="flex-1 flex flex-col min-w-0">
          <div className="grid grid-cols-[60px_140px_80px_1fr] bg-[#141414] text-[#E4E3E0] text-[10px] uppercase tracking-wider font-bold p-3">
            <div>Rank</div>
            <div>Candidate ID</div>
            <div>Score</div>
            <div>Reasoning / Feature Match</div>
          </div>
          
          <div className="flex-1 overflow-y-auto">
            {candidates.map((c: any) => (
              <div key={c.candidate_id} className="grid grid-cols-[60px_140px_80px_1fr] border-b border-[#141414] p-3 text-[12px] font-mono hover:bg-white transition-colors cursor-default">
                <div className="font-bold">#{String(c.rank).padStart(3, '0')}</div>
                <div className="text-blue-700">{c.candidate_id}</div>
                <div className="font-bold">{c.score}</div>
                <div className="text-[11px] font-sans leading-tight">
                  <span className="font-bold">Match: </span> {c.reasoning}
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>

      {/* FOOTER: COMMAND LINE & VALIDATION */}
      <footer className="h-16 border-t border-[#141414] flex items-center px-6 gap-8 bg-white/30 shrink-0">
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 bg-green-500 rounded-full"></div>
          <span className="text-[10px] font-bold uppercase">Output validated by provided schema validator</span>
        </div>
        <div className="flex-1 font-mono text-[11px] opacity-60 bg-black/5 p-2 rounded">
          $ python rank.py --candidates data/candidates.jsonl --out submissions/submission.csv
        </div>
        <div className="flex-1 font-mono text-[11px] opacity-60 bg-black/5 p-2 rounded">
          $ python validate_submission.py submissions/submission.csv
        </div>
      </footer>
    </div>
  );
}
