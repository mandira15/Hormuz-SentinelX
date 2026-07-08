import './style.css'

// Placeholder for the pipeline logic
document.querySelector('#trigger-pipeline')?.addEventListener('click', async () => {
  const btn = document.querySelector('#trigger-pipeline') as HTMLButtonElement;
  const scoreDisplay = document.querySelector('#ids-score') as HTMLElement;
  const briefDisplay = document.querySelector('#narrative-brief') as HTMLElement;
  
  btn.disabled = true;
  btn.textContent = 'Orchestrating Agents...';
  briefDisplay.innerHTML = '<p class="placeholder-text">Executing Multi-Agent Pipeline:<br>Geo -> Logistics -> Market -> Synthesis</p>';
  
  // Simulate API call to our new python backend endpoint
  setTimeout(() => {
    // This is where we would normally fetch('/api/brief')
    // Simulating the result of the pipeline:
    const mockIdsScore = "74.5";
    const mockBrief = `
      <h3>Executive Summary</h3>
      <p>The target economy demonstrates a critical <strong>IDS of 74.5</strong>, driven by high dependency on maritime imports via the Strait of Hormuz.</p>
      
      <h4>Geopolitical Assessment</h4>
      <p>Elevated risk due to regional instability. Diplomatic leverage is strained.</p>
      
      <h4>Logistics & Supply Chain</h4>
      <p>Chokepoint exposure is severe (85%). Alternative overland routes lack capacity to offset a maritime blockade.</p>
      
      <h4>Market Impact</h4>
      <p>Expected price volatility of 22% in crude commodities. Refineries are operating at 95% utilization with only 40 days of strategic reserves.</p>
    `;
    
    scoreDisplay.textContent = mockIdsScore;
    briefDisplay.innerHTML = mockBrief;
    
    btn.disabled = false;
    btn.textContent = 'Run AI Pipeline';
  }, 2500);
});
