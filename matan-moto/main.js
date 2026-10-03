/* ==========================================================
   מתן מוטו גרר - all editable values live here
   ========================================================== */
const CONFIG = {
  phone: "050-000-0000",          // placeholder - replace
  whatsapp: "972500000000",       // placeholder - replace (international format, no + or dashes)
  basePrice: 330,
  eta: "25 דקות",
  areas: ["ראשון לציון", "נס ציונה", "רחובות", "באר יעקב", "בית דגן"],
  hours: "א'-ה' 08:00-18:00, ו' 08:00-13:00", // placeholder - confirm with Matan
  payment: "ביט, פייבוקס, מזומן או כרטיס אשראי.", // placeholder - confirm with Matan

  messages: {
    whatsapp: "היי מתן, אני צריך גרירה לאופנוע. המיקום שלי: ",
    b2b: "היי מתן, אני מ[שם העסק] ורוצה לדבר על שיתוף פעולה"
  },

  // Google Ads conversions. TODO: replace with the real IDs from Google Ads
  // (Tools > Conversions > the action > Tag setup > "send_to").
  conversions: {
    call: "AW-XXXXXXXXXX/CALL_LABEL",
    whatsapp: "AW-XXXXXXXXXX/WHATSAPP_LABEL"
  },

  // Photos: to swap a placeholder for a real photo, set its path. One line each.
  // e.g. 1: "assets/photo-1.jpg"
  photos: {
    1: "", // מעמיס קטנוע על הנגרר, מבט מהצד
    2: "", // תקריב של רצועת קשירה על הגלגל
    3: "", // מתן בחולצת המותג ליד הנגרר
    4: "", // אופנוע קשור, מבט מאחור
    5: "", // מסירה ללקוח ליד מוסך
    6: ""  // הנגרר ריק ונקי
  }
};

(function () {
  "use strict";

  const telHref = "tel:" + CONFIG.phone.replace(/[^\d+]/g, "");
  const waHref = (text) => "https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(text);

  /* Links */
  document.querySelectorAll('[data-action="call"]').forEach((a) => { a.href = telHref; });
  document.querySelectorAll('[data-action="whatsapp"]').forEach((a) => { a.href = waHref(CONFIG.messages.whatsapp); });
  document.querySelectorAll('[data-action="whatsapp-b2b"]').forEach((a) => { a.href = waHref(CONFIG.messages.b2b); });

  /* Text values */
  const setText = (key, value) => {
    document.querySelectorAll('[data-cfg="' + key + '"]').forEach((el) => {
      if (el.textContent !== String(value)) el.textContent = value;
    });
  };
  setText("phone", CONFIG.phone);
  setText("price", CONFIG.basePrice);
  setText("etaNum", parseInt(CONFIG.eta, 10) || CONFIG.eta);
  setText("hours", CONFIG.hours);
  setText("payment", CONFIG.payment);
  setText("areas", CONFIG.areas.join(", "));

  const chips = document.getElementById("area-chips");
  if (chips) {
    const tpl = chips.querySelector(".chip");
    const current = Array.from(chips.querySelectorAll(".chip")).map((c) => c.textContent.trim()).join("|");
    if (tpl && current !== CONFIG.areas.join("|")) {
      chips.textContent = "";
      CONFIG.areas.forEach((name) => {
        const li = tpl.cloneNode(true);
        li.lastChild.textContent = name;
        chips.appendChild(li);
      });
    }
  }

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  /* Keep JSON-LD in sync with CONFIG */
  const ld = document.getElementById("ld-business");
  if (ld) {
    try {
      const data = JSON.parse(ld.textContent);
      data.telephone = "+972-" + CONFIG.phone.replace(/^0/, "");
      data.priceRange = "₪" + CONFIG.basePrice + "+";
      data.areaServed = CONFIG.areas.map((name) => ({ "@type": "City", name }));
      ld.textContent = JSON.stringify(data);
    } catch (e) { /* leave static JSON-LD as is */ }
  }

  /* Photos */
  Object.keys(CONFIG.photos).forEach((n) => {
    const src = CONFIG.photos[n];
    if (!src) return;
    document.querySelectorAll('[data-photo="' + n + '"]').forEach((box) => {
      const ph = box.querySelector(".ph-text");
      const img = new Image();
      img.src = src;
      img.alt = ph ? ph.textContent : "";
      img.loading = "lazy";
      img.decoding = "async";
      img.width = 800;
      img.height = 600;
      box.textContent = "";
      box.appendChild(img);
    });
  });

  /* Conversion tracking (Google Ads) */
  function track(kind, label) {
    if (window.gtag) {
      // TODO: set the real conversion IDs in CONFIG.conversions
      window.gtag("event", "conversion", {
        send_to: CONFIG.conversions[kind],
        event_category: kind,
        event_label: label
      });
    }
  }
  document.addEventListener("click", (e) => {
    const a = e.target.closest("[data-action]");
    if (!a) return;
    const action = a.getAttribute("data-action");
    const where = a.closest("header, .hero, .callbar, .final, .b2b, footer, section");
    const label = where ? (where.className || where.tagName).toString().split(" ")[0] : "page";
    track(action === "call" ? "call" : "whatsapp", action + ":" + label);
  });

  /* ---------- Motion ---------- */
  const motionOK = window.matchMedia("(prefers-reduced-motion: no-preference)").matches;

  // Second rig drives in above the final CTA road
  const rig = document.getElementById("rig");
  const finalRoad = document.querySelector(".final-road");
  if (rig && finalRoad) {
    const clone = rig.cloneNode(true);
    clone.removeAttribute("id");
    finalRoad.prepend(clone);
    finalRoad.setAttribute("data-reveal-only", "");
  }

  // Count-up for the numbers bar
  function countUp(el) {
    const target = parseInt(el.textContent, 10);
    if (!target) return;
    const start = performance.now();
    const dur = 1100;
    const tick = (now) => {
      const t = Math.min(1, (now - start) / dur);
      el.textContent = Math.round(target * (1 - Math.pow(1 - t, 3)));
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  // Delivery dot travels along the map route
  function driveRoute(map) {
    const path = map.querySelector(".route");
    const dot = map.querySelector(".route-dot");
    if (!path || !dot || !path.getTotalLength) return;
    const len = path.getTotalLength();
    const start = performance.now() + 1000;
    const dur = 1600;
    const tick = (now) => {
      const t = Math.max(0, Math.min(1, (now - start) / dur));
      const e = t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      const pt = path.getPointAtLength(len * e);
      dot.setAttribute("cx", pt.x);
      dot.setAttribute("cy", pt.y);
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  const revealEls = document.querySelectorAll("[data-reveal], [data-reveal-only]");
  if (motionOK && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        el.classList.add("is-in");
        io.unobserve(el);
        el.querySelectorAll("[data-count]").forEach(countUp);
        if (el.classList.contains("map")) driveRoute(el);
      });
    }, { threshold: 0.18, rootMargin: "0px 0px -6% 0px" });
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-in"));
    const dot = document.querySelector(".route-dot");
    if (dot) { dot.setAttribute("cx", 276); dot.setAttribute("cy", 336); }
  }

  /* Mobile call bar: appears after scrolling past the hero */
  const bar = document.querySelector(".callbar");
  const hero = document.querySelector(".hero");
  if (bar && hero && "IntersectionObserver" in window) {
    const links = bar.querySelectorAll("a");
    new IntersectionObserver(([entry]) => {
      const show = !entry.isIntersecting && entry.boundingClientRect.top < 0;
      bar.classList.toggle("is-visible", show);
      bar.setAttribute("aria-hidden", show ? "false" : "true");
      links.forEach((l) => { if (show) l.removeAttribute("tabindex"); else l.setAttribute("tabindex", "-1"); });
    }, { threshold: 0 }).observe(hero);
  }
})();
