/* NPhones — interactions
   typewriter hero · cursor-reactive blobs · reveals · tilt · counters · nav */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add(reduced ? 'reduced-motion' : 'js');

  /* start reloads at the top — the animated hero replays, so restored
     scroll offsets would strand the headline under the fixed header.
     Mobile Chrome can restore scroll after initial script execution,
     so re-assert on load and pageshow too. */
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  function toTop() {
    if (!location.hash) window.scrollTo(0, 0);
  }
  toTop();
  window.addEventListener('load', function () { setTimeout(toTop, 0); });
  window.addEventListener('pageshow', function () { setTimeout(toTop, 0); });

  /* ---------- smooth inertia scrolling (Lenis) ---------- */
  if (!reduced && typeof Lenis !== 'undefined' && matchMedia('(pointer: fine)').matches) {
    document.documentElement.style.scrollBehavior = 'auto';
    var lenis = new Lenis({
      lerp: 0.075,
      wheelMultiplier: 0.85,
      smoothWheel: true
    });
    (function lenisRaf(time) {
      lenis.raf(time);
      requestAnimationFrame(lenisRaf);
    })(performance.now());
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var id = a.getAttribute('href');
        if (id.length > 1 && document.querySelector(id)) {
          e.preventDefault();
          lenis.scrollTo(id, { offset: -100, duration: 1.4 });
        }
      });
    });
  }

  /* ---------- 50/50 temperature rhythm: alternate cool/warm light sections ---------- */
  (function () {
    var i = 0;
    document.querySelectorAll('.section').forEach(function (sec) {
      if (sec.classList.contains('section-dark') || sec.classList.contains('section-forest')) return;
      sec.classList.remove('section-tint');
      sec.classList.add(i % 2 === 0 ? 'section-cool-auto' : 'section-warm-auto');
      /* warm sections get a cream blob companion */
      if (i % 2 === 1) {
        var blobs = sec.querySelector('.blobs');
        if (blobs) {
          var b = document.createElement('div');
          b.className = 'blob cream';
          b.dataset.depth = '0.06';
          b.style.cssText = 'width:300px;height:300px;top:35%;left:52%;';
          b.innerHTML = '<div class="blob-inner"></div>';
          blobs.appendChild(b);
        }
      }
      i++;
    });
    /* forest CTA panels get a warm cream glow to break the green monochrome */
    document.querySelectorAll('.section-forest .blobs').forEach(function (blobs) {
      var b = document.createElement('div');
      b.className = 'blob cream';
      b.dataset.depth = '0.05';
      b.style.cssText = 'width:380px;height:380px;bottom:-120px;left:18%;';
      b.innerHTML = '<div class="blob-inner"></div>';
      blobs.appendChild(b);
    });
  })();

  /* ---------- typewriter hero ---------- */
  var tw = document.getElementById('typewriter');
  if (tw) {
    var cursorEl = document.getElementById('type-cursor');
    var finalsWord = 'phones';
    var words = ['first...', 'second...', 'third...', finalsWord];

    function heroSettle() {
      var l2 = document.querySelector('.hero h1 .line2');
      if (l2) l2.classList.add('show');
      ['.hero-sub', '.hero-ctas', '.hero-note', '.phone-cta', '.phone-stage'].forEach(function (s) {
        var el = document.querySelector(s);
        if (el) el.classList.add('show');
      });
      if (cursorEl) setTimeout(function () { cursorEl.style.display = 'none'; }, 2400);
    }

    if (reduced) {
      tw.textContent = 'Your ' + finalsWord;
      heroSettle();
    } else {
      var wi = 0, ci = 0, deleting = false;
      var base = 'Your ';
      tw.textContent = base;
      function tick() {
        var w = words[wi];
        if (!deleting) {
          ci++;
          tw.textContent = base + w.slice(0, ci);
          if (ci === w.length) {
            if (wi === words.length - 1) { heroSettle(); return; }
            deleting = true;
            setTimeout(tick, 950);
            return;
          }
          setTimeout(tick, 75 + Math.random() * 60);
        } else {
          ci--;
          tw.textContent = base + w.slice(0, ci);
          if (ci === 0) { deleting = false; wi++; setTimeout(tick, 260); return; }
          setTimeout(tick, 38);
        }
      }
      setTimeout(tick, 650);
    }
  }

  /* ---------- cursor-reactive blobs ---------- */
  if (!reduced) {
    var blobs = [];
    document.querySelectorAll('.blob').forEach(function (b, i) {
      blobs.push({ el: b, depth: parseFloat(b.dataset.depth || (0.03 + (i % 3) * 0.025)), x: 0, y: 0, tx: 0, ty: 0 });
    });
    var mx = 0, my = 0;
    window.addEventListener('mousemove', function (e) {
      mx = e.clientX / window.innerWidth - 0.5;
      my = e.clientY / window.innerHeight - 0.5;
    }, { passive: true });
    (function blobLoop() {
      blobs.forEach(function (b) {
        b.tx = mx * b.depth * 1200;
        b.ty = my * b.depth * 1200;
        b.x += (b.tx - b.x) * 0.06;
        b.y += (b.ty - b.y) * 0.06;
        b.el.style.transform = 'translate(' + b.x.toFixed(1) + 'px,' + b.y.toFixed(1) + 'px)';
      });
      requestAnimationFrame(blobLoop);
    })();
  }

  /* ---------- scroll reveals: in AND out (desktop + mobile) ---------- */
  if (!reduced && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        en.target.classList.toggle('in', en.isIntersecting);
      });
    }, { threshold: 0, rootMargin: '-40px 0px -40px 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

    var sio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        en.target.classList.toggle('in', en.isIntersecting);
      });
    }, { threshold: 0, rootMargin: '-6% 0px -6% 0px' });
    document.querySelectorAll('.section').forEach(function (sec) {
      sec.classList.add('sec-anim');
      sio.observe(sec);
    });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- subpage hero typewriter (types once, no cycling) ---------- */
  var subH1 = document.querySelector('.page-first h1');
  if (subH1 && !tw) {
    if (!reduced) {
      var fullText = subH1.textContent;
      subH1.style.minHeight = subH1.offsetHeight + 'px';
      subH1.textContent = '';
      var subCur = document.createElement('span');
      subCur.className = 'type-cursor';
      subH1.appendChild(subCur);
      var si = 0;
      function subTick() {
        if (si < fullText.length) {
          subCur.insertAdjacentText('beforebegin', fullText.charAt(si));
          si++;
          setTimeout(subTick, 30 + Math.random() * 38);
        } else {
          setTimeout(function () { subCur.remove(); }, 1800);
        }
      }
      setTimeout(subTick, 350);
    }
  }

  /* ---------- glass card tilt ---------- */
  if (!reduced && matchMedia('(pointer: fine)').matches) {
    document.querySelectorAll('[data-tilt]').forEach(function (card) {
      card.addEventListener('mousemove', function (e) {
        var r = card.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = 'perspective(800px) rotateY(' + (px * 6) + 'deg) rotateX(' + (-py * 6) + 'deg) translateY(-4px)';
      });
      card.addEventListener('mouseleave', function () { card.style.transform = ''; });
    });

    var phone = document.querySelector('.phone');
    if (phone) {
      var stage = document.querySelector('.phone-stage');
      stage.addEventListener('mousemove', function (e) {
        var r = stage.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        phone.style.transform = 'rotateY(' + (px * 10) + 'deg) rotateX(' + (-py * 8) + 'deg)';
      });
      stage.addEventListener('mouseleave', function () { phone.style.transform = ''; });
    }
  }

  /* ---------- count-up stats ---------- */
  function animateCount(el) {
    var target = parseFloat(el.dataset.count);
    var suffix = el.dataset.suffix || '';
    var dur = 1600, t0 = null;
    function frame(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      p = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * p) + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }
  if (!reduced && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { animateCount(en.target); cio.unobserve(en.target); }
      });
    }, { threshold: 0.6 });
    document.querySelectorAll('[data-count]').forEach(function (el) { cio.observe(el); });
  } else {
    document.querySelectorAll('[data-count]').forEach(function (el) {
      el.textContent = el.dataset.count + (el.dataset.suffix || '');
    });
  }

  /* ---------- nav ---------- */
  var nav = document.querySelector('.nav');
  if (nav) {
    window.addEventListener('scroll', function () {
      nav.classList.toggle('scrolled', window.scrollY > 30);
    }, { passive: true });
    var burger = document.querySelector('.nav-burger');
    if (burger) burger.addEventListener('click', function () { nav.classList.toggle('open'); });
    nav.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('open'); });
    });
  }

  /* ---------- scroll-scrubbed deploy video ---------- */
  var scrubSection = document.querySelector('.video-scrub');
  var scrubVideo = document.getElementById('scrub-video');
  if (scrubSection && scrubVideo) {
    var phrases = scrubSection.querySelectorAll('.video-phrase');
    var dots = scrubSection.querySelectorAll('.video-dots span');

    function setPhase(p) {
      var idx = Math.min(2, Math.floor(p * 3));
      phrases.forEach(function (el, i) { el.classList.toggle('active', i === idx); });
      dots.forEach(function (el, i) { el.classList.toggle('active', i <= idx); });
    }

    if (reduced) {
      scrubVideo.setAttribute('controls', '');
      setPhase(0.99);
    } else {
      var curT = 0, ready = false;
      scrubVideo.addEventListener('loadedmetadata', function () { ready = true; });
      scrubVideo.load();
      (function scrubLoop() {
        var total = scrubSection.offsetHeight - window.innerHeight;
        if (ready && total > 0) {
          var rect = scrubSection.getBoundingClientRect();
          var p = Math.min(Math.max(-rect.top / total, 0), 1);
          var target = p * (scrubVideo.duration - 0.05);
          curT += (target - curT) * 0.14;
          if (Math.abs(scrubVideo.currentTime - curT) > 0.01) {
            try { scrubVideo.currentTime = curT; } catch (e) {}
          }
          setPhase(p);
        }
        requestAnimationFrame(scrubLoop);
      })();
    }
  }

  /* ---------- circular text orbit: follows cursor on desktop, pinned bottom-right on mobile ---------- */
  if (!reduced) {
    var ORBIT_TEXT = 'ONE DEVICE, NDLESS PHONES. ';
    var orbit = document.createElement('div');
    orbit.id = 'cursor-orbit';
    var ring = document.createElement('div');
    ring.className = 'orbit-ring';
    var chars = Array.from(ORBIT_TEXT);
    chars.forEach(function (ch, i) {
      var s = document.createElement('span');
      s.textContent = ch;
      s.style.setProperty('--a', ((360 / chars.length) * i).toFixed(2) + 'deg');
      ring.appendChild(s);
    });
    orbit.appendChild(ring);
    document.body.appendChild(orbit);

    /* pinned bottom-right on all devices; hover over interactive elements speeds it up */
    orbit.classList.add('visible');
    var angle = 0, speed = 360 / 20, targetSpeed = 360 / 20; /* deg per second */
    var lastT = performance.now();

    if (matchMedia('(pointer: fine)').matches) {
      document.addEventListener('mouseover', function (e) {
        targetSpeed = e.target.closest('a, button, input, .glass') ? 360 / 5 : 360 / 20;
      });
    }

    (function orbitLoop(t) {
      var dt = Math.min((t - lastT) / 1000, 0.05);
      lastT = t;
      speed += (targetSpeed - speed) * 0.08;
      angle = (angle + speed * dt) % 360;
      ring.style.transform = 'rotate(' + angle.toFixed(2) + 'deg)';
      requestAnimationFrame(orbitLoop);
    })(lastT);
  }

  /* ---------- hero phone: usable mini-Android ---------- */
  var heroPhone = document.querySelector('.hero .phone');
  var modeTag = document.getElementById('mode-tag');
  if (heroPhone && modeTag) {
    var personalMode = false;
    var autoSwitch = null;

    function setMode(p) {
      personalMode = p;
      heroPhone.classList.toggle('show-personal', p);
      modeTag.textContent = (p ? 'Personal phone' : 'Business phone') + ' · tap to switch';
    }
    function stopAuto() {
      if (autoSwitch) { clearInterval(autoSwitch); autoSwitch = null; }
    }
    if (!reduced) {
      autoSwitch = setInterval(function () { setMode(!personalMode); }, 4500);
    }
    modeTag.addEventListener('click', function () {
      stopAuto();
      setMode(!personalMode);
    });

    /* app screens inside the hero phone */
    var hpWa = document.getElementById('hp-wa');
    var hpMail = document.getElementById('hp-mail');
    var hpShot = document.getElementById('hp-shot');
    function hpClose() {
      [hpWa, hpMail, hpShot].forEach(function (s) { if (s) s.classList.remove('on'); });
    }
    heroPhone.querySelectorAll('[data-hp-close]').forEach(function (b) {
      b.addEventListener('click', hpClose);
    });
    heroPhone.querySelectorAll('.app[data-app]').forEach(function (b) {
      b.addEventListener('click', function () {
        stopAuto();
        var kind = b.dataset.app;
        if (kind === 'personal') {
          /* personal apps stay private — that's the point */
          b.classList.remove('shake'); void b.offsetWidth; b.classList.add('shake');
          return;
        }
        if (kind === 'wa' && hpWa) { hpWa.classList.add('on'); return; }
        if (kind === 'mail' && hpMail) { hpMail.classList.add('on'); return; }
        if (hpShot) {
          document.getElementById('hp-shot-title').textContent = b.dataset.name || 'App';
          hpShot.classList.add('on');
        }
      });
    });
    /* functional WhatsApp composer */
    var hpSend = document.getElementById('hp-send');
    var hpMsg = document.getElementById('hp-msg');
    if (hpSend && hpMsg) {
      function hpSendMsg() {
        var v = hpMsg.value.trim();
        if (!v) return;
        var chat = document.getElementById('hp-chat');
        var out = document.createElement('div');
        out.className = 'hpb out';
        out.textContent = v;
        chat.appendChild(out);
        hpMsg.value = '';
        chat.scrollTop = chat.scrollHeight;
        setTimeout(function () {
          var rep = document.createElement('div');
          rep.className = 'hpb in';
          rep.textContent = 'Got it, thanks!';
          chat.appendChild(rep);
          chat.scrollTop = chat.scrollHeight;
        }, 1100);
      }
      hpSend.addEventListener('click', hpSendMsg);
      hpMsg.addEventListener('keydown', function (e) { if (e.key === 'Enter') hpSendMsg(); });
    }
  }

  /* ---------- homepage use-case chip switcher ---------- */
  var ucChips = document.getElementById('uc-chips');
  if (ucChips) {
    var UC = [
      { k: 'Sales teams', t: 'The customer stays with the company.', x: 'A dedicated business number, WhatsApp Business, CRM and contacts for every rep — without another device.', l: ['Business contacts stay company property', 'Reassign a departing rep’s number in one click', 'Consistent company identity on every touchpoint'], h: 'uc-sales.html' },
      { k: 'Field service', t: 'The office, in the field.', x: 'Technicians and installers get service apps, work photos and a business number from one secure cloud phone.', l: ['Work-order and CRM apps in the business phone', 'Work photos never mix with personal galleries', 'Remove access remotely when contracts end'], h: 'uc-field.html' },
      { k: 'Logistics', t: 'Every driver connected. No fleet to manage.', x: 'Drivers and couriers reach customers on business numbers — without a second device in every glovebox.', l: ['Customer communication separated from personal life', 'Proof-of-delivery with the business camera', 'Zero device purchasing and replacement costs'], h: 'uc-logistics.html' },
      { k: 'Contractors', t: 'Access for the project. Not forever.', x: 'A complete business phone for exactly as long as the engagement lasts — then one click removes it.', l: ['No phones purchased for 3-month engagements', 'Activated the morning the project starts', 'Company data never leaves the business environment'], h: 'uc-contractors.html' },
      { k: 'Remote & global', t: 'One business identity. Any location.', x: 'Distributed employees get the same business phone wherever they operate — no local hardware, no number chaos.', l: ['Same business phone from any location or device', 'Consistent number across borders', 'International onboarding in minutes'], h: 'uc-remote.html' },
      { k: 'Government & defense', t: 'Sensitive work. Zero device risk.', x: 'Controlled mobile access for sensitive environments — operational data never touches a personal device.', l: ['Data remains inside the governed environment', 'Temporary personnel activated in minutes', 'On-premises deployment for closed networks'], h: 'uc-government.html' }
    ];
    var panel = document.getElementById('uc-panel');
    var ucT = document.getElementById('ucp-title');
    var ucX = document.getElementById('ucp-text');
    var ucL = document.getElementById('ucp-list');
    var ucA = document.getElementById('ucp-link');
    function setUC(i, instant) {
      function apply() {
        ucT.textContent = UC[i].t;
        ucX.textContent = UC[i].x;
        ucL.innerHTML = '';
        UC[i].l.forEach(function (li) {
          var el = document.createElement('li');
          el.textContent = li;
          ucL.appendChild(el);
        });
        ucA.href = UC[i].h;
        panel.classList.remove('swapping');
      }
      ucChips.querySelectorAll('.uc-chip').forEach(function (c, j) {
        c.classList.toggle('active', i === j);
        c.setAttribute('aria-selected', i === j ? 'true' : 'false');
      });
      if (instant || reduced) { apply(); return; }
      panel.classList.add('swapping');
      setTimeout(apply, 200);
    }
    UC.forEach(function (u, i) {
      var b = document.createElement('button');
      b.className = 'uc-chip';
      b.type = 'button';
      b.setAttribute('role', 'tab');
      b.textContent = u.k;
      b.addEventListener('click', function () { setUC(i); });
      ucChips.appendChild(b);
    });
    setUC(0, true);
  }

  /* ---------- demo form: conditional segments + submission ----------
     To receive leads by email:
     1. Create a free form at https://formspree.io (Forms → New form,
        set the recipient to contact@nphones.com or your inbox)
     2. Copy the form ID and paste the full endpoint below, e.g.
        FORM_ENDPOINT = 'https://formspree.io/f/xanyzabc';
     3. git push — done. Leads arrive as emails with all form fields. */
  var FORM_ENDPOINT = 'https://formspree.io/f/mrenzbgz';

  document.querySelectorAll('form[data-static]').forEach(function (f) {
    var org = f.querySelector('select[name="orgtype"]');
    if (org) {
      var subs = f.querySelectorAll('select[data-org]');
      function updSegs() {
        subs.forEach(function (s) {
          var active = s.dataset.org === org.value;
          s.hidden = !active;
          if (!active) s.selectedIndex = 0;
        });
      }
      org.addEventListener('change', updSegs);
      updSegs();
    }
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = f.parentElement.querySelector('.form-note');
      var btn = f.querySelector('button[type="submit"]');
      if (!FORM_ENDPOINT) {
        if (note) note.textContent = 'Form wiring pending — add your Formspree endpoint in assets/main.js.';
        return;
      }
      var data = new FormData(f);
      data.append('_subject', 'New demo request — nphones.com');
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
      fetch(FORM_ENDPOINT, {
        method: 'POST',
        body: data,
        headers: { 'Accept': 'application/json' }
      }).then(function (res) {
        if (res.ok) {
          f.reset();
          if (note) note.textContent = 'Thank you — we’ll be in touch within 24 hours.';
          if (btn) { btn.textContent = 'Request sent ✓'; }
        } else { throw new Error('bad status'); }
      }).catch(function () {
        if (note) note.textContent = 'Something went wrong — email us directly at contact@nphones.com.';
        if (btn) { btn.disabled = false; btn.textContent = 'Request a demo'; }
      });
    });
  });
})();
