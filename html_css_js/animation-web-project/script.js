// Part 2 & 3: JS functions demonstrating scope, params, returns, and animation triggers

/* ---------- Part 2: Scope, parameters, and return values ---------- */

/*
 Global state (example of a global variable).
 Changing this affects functions that reference it.
*/
let animationCount = 0; // global

// Simple pure function: takes parameters, returns a value
function add(a, b) {
  return a + b;
}

// Function demonstrating local scope vs global scope
function demoScope(name) {
  const localGreeting = `Hello, ${name}`; // local variable
  animationCount += 1; // modifies global state
  return { localGreeting, animationCount }; // returns an object
}

// Async helper that returns a Promise (useful for waiting between animations)
function delay(ms = 300) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Button that demonstrates function use
document.getElementById('calcBtn')?.addEventListener('click', () => {
  const sum = add(8, 14); // uses parameters and return value
  const scopeResult = demoScope('Student'); // shows local vs global
  const out = [
    `add(8,14) => ${sum}`,
    `demoScope('Student') => ${JSON.stringify(scopeResult)}`,
    `animationCount (global) => ${animationCount}`
  ].join('\n');
  const el = document.getElementById('calcOutput');
  if (el) el.textContent = out;
  console.info(out);
});

/* ---------- Part 3: Combining CSS with JS ---------- */

// Reusable function: toggles a class on an element by id and returns boolean status
function toggleClassById(id, className) {
  const el = document.getElementById(id);
  if (!el) return false;
  el.classList.toggle(className);
  return el.classList.contains(className);
}

// Animate a box by adding a class for a duration, then removing it
async function animateBox(boxId, duration = 800) {
  const applied = toggleClassById(boxId, 'animate');
  // Return a promise that resolves when animation is "complete"
  await delay(duration);
  // Remove the class so it can be re-triggered later
  const el = document.getElementById(boxId);
  if (el) el.classList.remove('animate');
  return applied;
}

// Flip card function that accepts id and returns new state
function flipCard(cardId) {
  const flipped = toggleClassById(cardId, 'flipped');
  return flipped;
}

// Modal open/close functions using aria-hidden (accessible)
function openModal(id) {
  const modal = document.getElementById(id);
  if (!modal) return false;
  modal.setAttribute('aria-hidden', 'false');
  return true;
}
function closeModal(id) {
  const modal = document.getElementById(id);
  if (!modal) return false;
  modal.setAttribute('aria-hidden', 'true');
  return true;
}

// Loader play/pause toggle (demonstrates modifying element style)
function toggleLoader(loaderId) {
  const loader = document.getElementById(loaderId);
  if (!loader) return false;
  const isRunning = getComputedStyle(loader).animationPlayState === 'running';
  loader.style.animationPlayState = isRunning ? 'paused' : 'running';
  loader.setAttribute('aria-hidden', String(isRunning));
  return !isRunning;
}

/* ---------- Event wiring: keep minimal and reusable ---------- */

document.getElementById('animBox')?.addEventListener('click', () => {
  // animateBox is reusable; it returns a Promise that resolves when done
  animateBox('animBox', 900).then(() => {
    console.log('Box animation finished');
  });
});

document.getElementById('flipBtn')?.addEventListener('click', () => {
  const state = flipCard('card');
  console.log('Card flipped?', state);
});

document.getElementById('card')?.addEventListener('click', () => {
  const state = flipCard('card'); // card itself can be clicked to flip
  console.log('Card flipped (click on card)?', state);
});

document.getElementById('openModal')?.addEventListener('click', () => openModal('modal'));
document.getElementById('closeModal')?.addEventListener('click', () => closeModal('modal'));
document.getElementById('toggleLoader')?.addEventListener('click', () => {
  const running = toggleLoader('loader');
  console.log('Loader running?', running);
});

/* ---------- Small demonstration: auto-toggle the loader once on load ---------- */
window.addEventListener('load', async () => {
  // start loader briefly to show combined behavior
  toggleLoader('loader'); // start
  await delay(1500);
  toggleLoader('loader'); // stop
});