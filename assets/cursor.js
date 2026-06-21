(function () {
    var footerLinks = [
        { href: "/", label: "Home" },
        { href: "/diagai", label: "DiagAI" },
        { href: "/cie_pro", label: "CIE Pro" },
        { href: "/helix", label: "HELIX" },
        { href: "/hexx", label: "Hexx" },
        { href: "/mdx", label: "MDX" },
        { href: "/xhandbook", label: "XHandbook" },
        { href: "/pricing", label: "Pricing" },
        { href: "/docs", label: "Docs" },
        { href: "/about", label: "About" },
        { href: "/solutions", label: "Solutions" },
        { href: "/case_studies", label: "Case Studies" },
        { href: "/blog/", label: "Blog" },
        { href: "/contact_us", label: "Contact" },
        { href: "/privacy", label: "Privacy" },
        { href: "/terms", label: "Terms" },
        { href: "/security", label: "Security" }
    ];

    function ensureFooterNavigation() {
        var footer = document.querySelector("footer");
        if (footer) {
            return;
        }

        footer = document.createElement("footer");
        footer.className = "vl-site-footer";
        document.body.classList.add("vl-has-generated-footer");
        document.body.appendChild(footer);

        var directory = document.createElement("div");
        directory.className = "vl-footer-directory";
        directory.setAttribute("aria-label", "Site directory");

        var heading = document.createElement("p");
        heading.className = "vl-footer-directory-title";
        heading.textContent = "Vehicle Lab";
        directory.appendChild(heading);

        var nav = document.createElement("nav");
        nav.className = "vl-footer-directory-links";
        footerLinks.forEach(function (link) {
            var anchor = document.createElement("a");
            anchor.href = link.href;
            anchor.textContent = link.label;
            nav.appendChild(anchor);
        });
        directory.appendChild(nav);

        var copyright = document.createElement("p");
        copyright.className = "vl-footer-directory-copy";
        copyright.textContent = "\u00a9 2026 Vehicle Lab. All rights reserved.";
        directory.appendChild(copyright);
        footer.appendChild(directory);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", ensureFooterNavigation, { once: true });
    } else {
        ensureFooterNavigation();
    }
}());

(function () {
    var root = document.documentElement;
    var media = window.matchMedia("(hover: hover) and (pointer: fine)");
    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    if (!media.matches || reducedMotion.matches) {
        return;
    }

    function getAccentColor() {
        var configured = window.tailwind &&
            window.tailwind.config &&
            window.tailwind.config.theme &&
            window.tailwind.config.theme.extend &&
            window.tailwind.config.theme.extend.colors &&
            window.tailwind.config.theme.extend.colors.primary;

        if (configured) {
            return configured;
        }

        var probe = document.createElement("span");
        probe.className = "text-primary";
        probe.style.cssText = "position:absolute;visibility:hidden;pointer-events:none;";
        document.body.appendChild(probe);
        var color = window.getComputedStyle(probe).color;
        probe.remove();

        return color || "#00e5ff";
    }

    function initCursor() {
        if (document.querySelector(".vl-cursor-dot")) {
            return;
        }

        root.style.setProperty("--vl-cursor-accent", getAccentColor());
        var dot = document.createElement("div");
        var ring = document.createElement("div");
        dot.className = "vl-cursor-dot";
        ring.className = "vl-cursor-ring";
        document.body.appendChild(ring);
        document.body.appendChild(dot);

        var pointer = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
        var lead = { x: pointer.x, y: pointer.y };
        var follower = { x: pointer.x, y: pointer.y };
        var hoverScale = 1;
        var targetScale = 1;
        var previousFrame = performance.now();
        var rafId = null;

        function easingForDuration(deltaMs, durationMs) {
            return reducedMotion.matches ? 1 : 1 - Math.pow(0.001, deltaMs / durationMs);
        }

        function draw(now) {
            var deltaMs = Math.min(64, now - previousFrame);
            previousFrame = now;
            var leadEase = easingForDuration(deltaMs, 300);
            var followerEase = easingForDuration(deltaMs, 700);
            lead.x += (pointer.x - lead.x) * leadEase;
            lead.y += (pointer.y - lead.y) * leadEase;
            follower.x += (pointer.x - follower.x) * followerEase;
            follower.y += (pointer.y - follower.y) * followerEase;
            hoverScale += (targetScale - hoverScale) * easingForDuration(deltaMs, 300);

            dot.style.transform = "translate3d(" + lead.x + "px, " + lead.y + "px, 0) translate(-50%, -50%)";
            ring.style.transform = "translate3d(" + follower.x + "px, " + follower.y + "px, 0) translate(-50%, -50%) scale(" + hoverScale + ")";

            rafId = window.requestAnimationFrame(draw);
        }

        function setHoverState(event) {
            var target = event.target;
            var interactiveItem = target && target.closest("a, button, [role='button'], [data-cursor], [data-magnetic]");
            var isInteractive = !!interactiveItem;
            root.classList.toggle("vl-cursor-hover", isInteractive);
            targetScale = isInteractive ? 2.67 : 1;
        }

        document.addEventListener("pointermove", function (event) {
            pointer.x = event.clientX;
            pointer.y = event.clientY;
            root.classList.add("vl-cursor-visible");
            setHoverState(event);
        }, { passive: true });

        document.addEventListener("pointerleave", function () {
            root.classList.remove("vl-cursor-visible", "vl-cursor-hover");
        });

        document.addEventListener("pointerover", setHoverState, { passive: true });
        document.addEventListener("pointerout", function (event) {
            setHoverState(event);
        }, { passive: true });

        document.addEventListener("focusin", function (event) {
            if (event.target && event.target.closest("a, button, [role='button'], [data-cursor], [data-magnetic]")) {
                root.classList.add("vl-cursor-hover");
                targetScale = 2.67;
            }
        });

        document.addEventListener("focusout", function () {
            root.classList.remove("vl-cursor-hover");
            targetScale = 1;
        });

        root.classList.add("vl-cursor-ready");
        rafId = window.requestAnimationFrame(draw);

        media.addEventListener("change", function (event) {
            if (!event.matches && rafId) {
                window.cancelAnimationFrame(rafId);
                root.classList.remove("vl-cursor-ready", "vl-cursor-visible", "vl-cursor-hover");
                dot.remove();
                ring.remove();
            }
        });

        reducedMotion.addEventListener("change", function (event) {
            if (event.matches && rafId) {
                window.cancelAnimationFrame(rafId);
                root.classList.remove("vl-cursor-ready", "vl-cursor-visible", "vl-cursor-hover");
                dot.remove();
                ring.remove();
            }
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initCursor, { once: true });
    } else {
        initCursor();
    }
}());
