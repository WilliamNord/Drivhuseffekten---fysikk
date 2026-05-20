import * as e from "@wordpress/interactivity";

var t = {
	d: (e, n) => {
		for (var o in n) {
			if (t.o(n, o) && !t.o(e, o)) {
				Object.defineProperty(e, o, {
					enumerable: true,
					get: n[o],
				});
			}
		}
	},
	o: (e, t) => Object.prototype.hasOwnProperty.call(e, t),
};

const n = ((e) => {
	var n = {};
	return t.d(n, e), n;
})({
	getContext: () => e.getContext,
	getElement: () => e.getElement,
	store: () => e.store,
	withSyncEvent: () => e.withSyncEvent,
});

const o = [
	"a[href]",
	'input:not([disabled]):not([type="hidden"]):not([aria-hidden])',
	"select:not([disabled]):not([aria-hidden])",
	"textarea:not([disabled]):not([aria-hidden])",
	"button:not([disabled]):not([aria-hidden])",
	"[contenteditable]",
	'[tabindex]:not([tabindex^="-"])',
];

document.addEventListener("click", () => {});

const { state: l, actions: c } = (0, n.store)(
	"core/navigation",
	{
		state: {
			get roleAttribute() {
				return (0, n.getContext)().type === "overlay" && l.isMenuOpen
					? "dialog"
					: null;
			},

			get ariaModal() {
				return (0, n.getContext)().type === "overlay" && l.isMenuOpen
					? "true"
					: null;
			},

			get ariaLabel() {
				const e = (0, n.getContext)();

				return e.type === "overlay" && l.isMenuOpen
					? e.ariaLabel
					: null;
			},

			get isMenuOpen() {
				return Object.values(l.menuOpenedBy).filter(Boolean).length > 0;
			},

			get menuOpenedBy() {
				const e = (0, n.getContext)();

				return e.type === "overlay"
					? e.overlayOpenedBy
					: e.submenuOpenedBy;
			},
		},

		actions: {
			openMenuOnHover() {
				const {
					type: e,
					overlayOpenedBy: t,
				} = (0, n.getContext)();

				if (
					e === "submenu" &&
					Object.values(t || {}).filter(Boolean).length === 0
				) {
					c.openMenu("hover");
				}
			},

			closeMenuOnHover() {
				const {
					type: e,
					overlayOpenedBy: t,
				} = (0, n.getContext)();

				if (
					e === "submenu" &&
					Object.values(t || {}).filter(Boolean).length === 0
				) {
					c.closeMenu("hover");
				}
			},

			openMenuOnClick() {
				const e = (0, n.getContext)();
				const { ref: t } = (0, n.getElement)();

				e.previousFocus = t;

				c.openMenu("click");
			},

			closeMenuOnClick() {
				c.closeMenu("click");
				c.closeMenu("focus");
			},

			openMenuOnFocus() {
				c.openMenu("focus");
			},

			toggleMenuOnClick() {
				const e = (0, n.getContext)();
				const { ref: t } = (0, n.getElement)();

				if (window.document.activeElement !== t) {
					t.focus();
				}

				const { menuOpenedBy: o } = l;

				if (o.click || o.focus) {
					c.closeMenu("click");
					c.closeMenu("focus");
				} else {
					e.previousFocus = t;
					c.openMenu("click");
				}
			},

			handleMenuKeydown: (0, n.withSyncEvent)((e) => {
				const {
					type: t,
					firstFocusableElement: o,
					lastFocusableElement: u,
				} = (0, n.getContext)();

				if (l.menuOpenedBy.click) {
					if (e.key === "Escape") {
						e.stopPropagation();

						c.closeMenu("click");
						c.closeMenu("focus");

						return;
					}

					if (t === "overlay" && e.key === "Tab") {
						if (
							e.shiftKey &&
							window.document.activeElement === o
						) {
							e.preventDefault();
							u.focus();
						} else if (
							!e.shiftKey &&
							window.document.activeElement === u
						) {
							e.preventDefault();
							o.focus();
						}
					}
				}
			}),

			handleMenuFocusout: (0, n.withSyncEvent)((e) => {
				const {
					modal: t,
					type: o,
				} = (0, n.getContext)();

				if (
					(e.relatedTarget === null ||
						(!t?.contains(e.relatedTarget) &&
							e.target !==
								window.document.activeElement)) &&
					o === "submenu"
				) {
					c.closeMenu("click");
					c.closeMenu("focus");
				}
			}),

			openMenu(e = "click") {
				const { type: t } = (0, n.getContext)();

				l.menuOpenedBy[e] = true;

				if (t === "overlay") {
					document.documentElement.classList.add(
						"has-modal-open"
					);
				}
			},

			closeMenu(e = "click") {
				const t = (0, n.getContext)();

				l.menuOpenedBy[e] = false;

				if (!l.isMenuOpen) {
					if (
						t.modal?.contains(window.document.activeElement)
					) {
						t.previousFocus?.focus();
					}

					t.modal = null;
					t.previousFocus = null;

					if (t.type === "overlay") {
						document.documentElement.classList.remove(
							"has-modal-open"
						);
					}
				}
			},
		},

		callbacks: {
			initMenu() {
				const e = (0, n.getContext)();
				const { ref: t } = (0, n.getElement)();

				if (l.isMenuOpen) {
					const n = t.querySelectorAll(o);

					e.modal = t;
					e.firstFocusableElement = n[0];
					e.lastFocusableElement = n[n.length - 1];
				}
			},

			focusFirstElement() {
				const { ref: e } = (0, n.getElement)();

				if (l.isMenuOpen) {
					const t = e.querySelectorAll(o);

					t?.[0]?.focus();
				}
			},
		},
	},
	{ lock: true }
);