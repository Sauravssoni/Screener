import { useEffect, useState } from "react";

export default function App() {
  const [candidates, setCandidates] = useState([]);
  const [summary, setSummary] = useState(null);
  const [selectedCandidate, setSelectedCandidate] = useState(null);
  const [reviewQueue, setReviewQueue] = useState([]);

  useEffect(() => {
    fetch("/reports/dashboard_top10.json")
      .then((res) => {
        if (!res.ok) throw new Error("Run ranking pipeline first");
        return res.json();
      })
      .then((data) => setCandidates(data))
      .catch((err) => console.log(err));

    fetch("/reports/run_summary.json")
      .then((res) => res.json())
      .then((data) => setSummary(data))
      .catch((err) => console.log(err));

    fetch("/reports/human_review_queue.json")
      .then((res) => res.json())
      .then((data) => setReviewQueue(data))
      .catch((err) => console.log(err));
  }, []);

  const handleStatusChange = (candidateId, newStatus) => {
    // Optimistic UI update
    setReviewQueue((prev) =>
      prev.map(c => c.candidate_id === candidateId ? { ...c, status: newStatus } : c)
    );
    // Note: In a real system we would POST to a backend here.
    // For this static demo we update React state, mirroring demo-safe actions.
  };

  const getStatusForCandidate = (id) => {
    const item = reviewQueue.find(c => c.candidate_id === id);
    return item ? item.status : "pending_review";
  };

  if (!summary || candidates.length === 0) {
    return (
      <div className="flex h-screen items-center justify-center bg-gray-50 text-gray-800">
        <h1 className="text-xl">Run ranking pipeline first to generate reports.</h1>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-screen w-full bg-slate-50 text-slate-800 font-sans border-t-4 border-emerald-600 overflow-hidden">
      {/* HEADER */}
      <header className="bg-white border-b border-slate-200 px-6 py-4 flex items-center justify-between shadow-sm shrink-0">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight text-slate-900">RedrobRank RecruiterOps Console</h1>
          <p className="text-sm text-slate-500 font-medium tracking-wide uppercase mt-1">Validated CPU-only TalentOps Agent</p>
        </div>

        <div className="flex gap-6">
          <div className="bg-slate-50 rounded border border-slate-200 px-4 py-2 flex flex-col items-start min-w-32">
            <span className="text-xs uppercase text-slate-500 font-semibold mb-1">Candidates Processed</span>
            <span className="font-mono text-lg text-slate-900">{summary.candidates_processed.toLocaleString()}</span>
          </div>
          <div className="bg-slate-50 rounded border border-slate-200 px-4 py-2 flex flex-col items-start min-w-32">
            <span className="text-xs uppercase text-slate-500 font-semibold mb-1">Runtime</span>
            <span className="font-mono text-lg text-slate-900">{summary.runtime_seconds}s</span>
          </div>
          <div className="bg-slate-50 rounded border border-slate-200 px-4 py-2 flex flex-col items-start min-w-32">
            <span className="text-xs uppercase text-slate-500 font-semibold mb-1">Validator Status</span>
            <span className="font-mono text-lg text-emerald-600 font-bold uppercase">{summary.validator_status}</span>
          </div>
          <div className="bg-slate-50 rounded border border-slate-200 px-4 py-2 flex flex-col items-start min-w-32">
            <span className="text-xs uppercase text-slate-500 font-semibold mb-1">Top-100 Trap Flags</span>
            <span className="font-mono text-lg text-amber-600 font-bold">{summary.top100_trap_count}</span>
          </div>
          <div className="bg-slate-50 rounded border border-slate-200 px-4 py-2 flex flex-col items-start min-w-32">
            <span className="text-xs uppercase text-slate-500 font-semibold mb-1">Network Calls</span>
            <span className="font-mono text-lg text-slate-900 uppercase">Disabled</span>
          </div>
        </div>
      </header>

      {/* TIMELINE */}
      <div className="bg-slate-100 border-b border-slate-200 px-6 py-2 flex items-center gap-8 text-xs font-semibold text-slate-500 uppercase tracking-wider shrink-0">
        <span className="text-emerald-700">✓ JD Parsed</span>
        <span>→</span>
        <span className="text-emerald-700">✓ Evidence Extracted</span>
        <span>→</span>
        <span className="text-emerald-700">✓ Candidates Scored</span>
        <span>→</span>
        <span className="text-emerald-700">✓ Traps Filtered</span>
        <span>→</span>
        <span className="text-emerald-700">✓ Shortlist Validated</span>
        <span>→</span>
        <span className="text-amber-600">Pending Human Review</span>
        <span>→</span>
        <span className="text-slate-400">Outreach Locked</span>
      </div>

      {/* MAIN CONTENT AREA */}
      <main className="flex flex-1 overflow-hidden">
        {/* LEFT PANEL: Job Intelligence */}
        <aside className="w-64 bg-white border-r border-slate-200 p-6 flex flex-col overflow-y-auto">
          <h2 className="text-xs font-bold uppercase text-slate-400 tracking-wider mb-6">Job Intelligence</h2>
          <div className="space-y-6">
            <div>
              <h3 className="text-sm font-semibold text-slate-800 mb-1">Role</h3>
              <p className="text-sm text-slate-600">Senior AI Engineer — Founding Team</p>
            </div>
            <div>
              <h3 className="text-sm font-semibold text-slate-800 mb-2">Must-Haves</h3>
              <ul className="text-sm text-slate-600 space-y-1 list-disc list-inside">
                <li>Core AI / Retrieval</li>
                <li>Production Experience</li>
                <li>Evaluation Frameworks</li>
                <li>Python Systems</li>
              </ul>
            </div>
            <div>
              <h3 className="text-sm font-semibold text-slate-800 mb-2">Production Expectations</h3>
              <p className="text-sm text-slate-600">Must demonstrate deploying models or pipelines to real users with latency/scale considerations.</p>
            </div>
            <div>
              <h3 className="text-sm font-semibold text-slate-800 mb-2">Evaluation Expectations</h3>
              <p className="text-sm text-slate-600">Must show offline benchmarking (NDCG, MAP) and online A/B testing awareness.</p>
            </div>
            <div>
              <h3 className="text-sm font-semibold text-slate-800 mb-2">Location Constraints</h3>
              <p className="text-sm text-slate-600">Pune, Noida, Delhi, Gurgaon, Bangalore, or willing to relocate.</p>
            </div>
          </div>
        </aside>

        {/* CENTER: Ranked Shortlist Table */}
        <section className="flex-1 flex flex-col bg-slate-50 min-w-0 border-r border-slate-200">
          <div className="p-6 pb-2">
            <h2 className="text-lg font-semibold text-slate-800">Ranked Shortlist (Top 10)</h2>
          </div>
          
          <div className="flex-1 overflow-auto p-6 pt-0">
            <table className="w-full text-left text-sm whitespace-nowrap">
              <thead className="text-xs uppercase bg-slate-100 text-slate-500 tracking-wider sticky top-0">
                <tr>
                  <th className="p-3 font-semibold rounded-tl-lg">Rank</th>
                  <th className="p-3 font-semibold">Candidate ID</th>
                  <th className="p-3 font-semibold">Score</th>
                  <th className="p-3 font-semibold">Fit Band</th>
                  <th className="p-3 font-semibold">Evidence Tags</th>
                  <th className="p-3 font-semibold">Risk Flags</th>
                  <th className="p-3 font-semibold rounded-tr-lg">Review Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 bg-white">
                {candidates.map((c) => {
                  const status = getStatusForCandidate(c.candidate_id);
                  return (
                    <tr
                      key={c.candidate_id}
                      className={`hover:bg-slate-50 cursor-pointer transition-colors ${selectedCandidate?.candidate_id === c.candidate_id ? 'bg-emerald-50' : ''}`}
                      onClick={() => setSelectedCandidate(c)}
                    >
                      <td className="p-3 font-medium text-slate-900">{c.rank}</td>
                      <td className="p-3 font-mono text-emerald-700">{c.candidate_id}</td>
                      <td className="p-3 font-mono text-slate-700">{c.score}</td>
                      <td className="p-3">
                        <span className="px-2 py-1 rounded text-xs font-medium bg-emerald-100 text-emerald-800">
                          {c.fit_band}
                        </span>
                      </td>
                      <td className="p-3">
                        <div className="flex gap-1 flex-wrap">
                          {c.evidence_tags?.map((tag, i) => (
                            <span key={i} className="px-2 py-0.5 bg-slate-100 text-slate-600 text-xs rounded border border-slate-200">{tag}</span>
                          ))}
                        </div>
                      </td>
                      <td className="p-3 text-amber-600 text-xs">
                        {c.risk_flags?.length > 0 ? `${c.risk_flags.length} flag(s)` : 'None'}
                      </td>
                      <td className="p-3">
                        <span className={`px-2 py-1 rounded text-xs font-semibold capitalize ${
                          status === 'approved' ? 'bg-emerald-100 text-emerald-700' :
                          status === 'rejected' ? 'bg-red-100 text-red-700' :
                          status === 'hold' ? 'bg-amber-100 text-amber-700' :
                          'bg-slate-100 text-slate-500'
                        }`}>
                          {status.replace('_', ' ')}
                        </span>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </section>

        {/* RIGHT PANEL: Candidate Evidence Dossier */}
        <aside className="w-[400px] bg-white flex flex-col overflow-y-auto shrink-0 shadow-[-4px_0_15px_-3px_rgba(0,0,0,0.05)]">
          {selectedCandidate ? (
            <div className="p-6 flex flex-col h-full">
              <div className="mb-6 pb-6 border-b border-slate-100">
                <h2 className="text-xs font-bold uppercase text-slate-400 tracking-wider mb-2">Candidate Evidence Dossier</h2>
                <div className="font-mono text-xl text-emerald-700 font-bold mb-1">{selectedCandidate.candidate_id}</div>
                <div className="text-sm text-slate-500">Rank: #{selectedCandidate.rank} | Score: {selectedCandidate.score}</div>
              </div>

              <div className="space-y-6 flex-1">
                <div>
                  <h3 className="text-sm font-semibold text-slate-800 mb-2">Fit Explanation</h3>
                  <p className="text-sm text-slate-600 leading-relaxed bg-slate-50 p-3 rounded border border-slate-100">
                    {selectedCandidate.reasoning}
                  </p>
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-slate-50 p-3 rounded border border-slate-100">
                    <h3 className="text-xs font-semibold text-slate-500 uppercase tracking-wide mb-1">Production Evidence</h3>
                    <p className="font-mono text-slate-800 text-sm">Found {selectedCandidate.evidence_tags?.[1]?.split(': ')[1] || 0} signals</p>
                  </div>
                  <div className="bg-slate-50 p-3 rounded border border-slate-100">
                    <h3 className="text-xs font-semibold text-slate-500 uppercase tracking-wide mb-1">Eval Evidence</h3>
                    <p className="font-mono text-slate-800 text-sm">Found {selectedCandidate.evidence_tags?.[2]?.split(': ')[1] || 0} signals</p>
                  </div>
                </div>

                <div>
                  <h3 className="text-sm font-semibold text-slate-800 mb-2">Risk Flags</h3>
                  {selectedCandidate.risk_flags && selectedCandidate.risk_flags.length > 0 ? (
                    <ul className="text-sm text-amber-700 space-y-1 list-disc list-inside bg-amber-50 p-3 rounded border border-amber-100">
                      {selectedCandidate.risk_flags.map((flag, idx) => (
                        <li key={idx}>{flag}</li>
                      ))}
                    </ul>
                  ) : (
                    <p className="text-sm text-slate-500 italic">No honeypots or risk flags detected.</p>
                  )}
                </div>
              </div>

              <div className="mt-8 pt-6 border-t border-slate-100 flex flex-col gap-3">
                <h3 className="text-xs font-semibold text-slate-500 uppercase tracking-wide text-center">Human Review Checkpoint</h3>
                <div className="grid grid-cols-3 gap-2">
                  <button
                    onClick={() => handleStatusChange(selectedCandidate.candidate_id, "approved")}
                    className="py-2 px-4 rounded bg-emerald-600 hover:bg-emerald-700 text-white text-sm font-semibold transition-colors shadow-sm"
                  >
                    Approve
                  </button>
                  <button
                    onClick={() => handleStatusChange(selectedCandidate.candidate_id, "hold")}
                    className="py-2 px-4 rounded bg-amber-500 hover:bg-amber-600 text-white text-sm font-semibold transition-colors shadow-sm"
                  >
                    Hold
                  </button>
                  <button
                    onClick={() => handleStatusChange(selectedCandidate.candidate_id, "rejected")}
                    className="py-2 px-4 rounded bg-slate-200 hover:bg-slate-300 text-slate-800 text-sm font-semibold transition-colors"
                  >
                    Reject
                  </button>
                </div>
                <button className="py-2 px-4 rounded border border-slate-300 hover:bg-slate-50 text-slate-600 text-sm font-medium transition-colors mt-2" disabled>
                  Export Recruiter Packet (Requires Approval)
                </button>
              </div>
            </div>
          ) : (
            <div className="flex h-full items-center justify-center p-6 text-center">
              <p className="text-slate-400 text-sm">Select a candidate from the shortlist to view evidence and action.</p>
            </div>
          )}
        </aside>
      </main>
    </div>
  );
}
