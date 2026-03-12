// ── Init AOS ──────────────────────────────
AOS.init({
    duration: 800,
    easing: 'ease-out-cubic',
    once: true,
    offset: 60
});

// ── Register GSAP Plugins ─────────────────
gsap.registerPlugin(ScrollTrigger);

// ── Year ──────────────────────────────────
document.getElementById('year').textContent = new Date().getFullYear();

// ── Typing Animation ──────────────────────
const phrases = [
    'build scalable full-stack web applications.',
    'solve 400+ DSA problems on LeetCode.',
    'develop modern React & Node.js apps.',
    'design clean and responsive interfaces.',
    'turn ideas into real digital products.'
];
const typedEl = document.getElementById('typed-text');
let phraseIdx = 0,
    charIdx = 0,
    deleting = false;

function typeLoop() {
    const current = phrases[phraseIdx];
    if (!deleting) {
        typedEl.textContent = current.slice(0, charIdx + 1);
        charIdx++;
        if (charIdx === current.length) {
            deleting = true;
            setTimeout(typeLoop, 1800);
            return;
        }
        setTimeout(typeLoop, 60);
    } else {
        typedEl.textContent = current.slice(0, charIdx - 1);
        charIdx--;
        if (charIdx === 0) {
            deleting = false;
            phraseIdx = (phraseIdx + 1) % phrases.length;
            setTimeout(typeLoop, 400);

            return;
        }
        setTimeout(typeLoop, 35);
    }
}
typeLoop();

// ── Hamburger Menu ────────────────────────
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');
const header = document.getElementById('header');

function closeMenu() {
    hamburger.classList.remove('active');
    mobileNav.classList.remove('open');
}

function openMenu() {
    hamburger.classList.add('active');
    mobileNav.classList.add('open');
}

hamburger.addEventListener('click', (e) => {
    e.stopPropagation();
    e.preventDefault();
    if (mobileNav.classList.contains('open')) {
        closeMenu();
    } else {
        openMenu();
    }
});

// Close menu when a mobile link is clicked
mobileNav.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', closeMenu);
});

// Close menu when clicking outside the header
document.addEventListener('click', (e) => {
    if (mobileNav.classList.contains('open') && !header.contains(e.target)) {
        closeMenu();
    }
});

// Close menu on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileNav.classList.contains('open')) {
        closeMenu();
    }
});

// ── Scroll Progress ───────────────────────
const progressBar = document.getElementById('scrollProgress');

window.addEventListener('scroll', () => {
    const h = document.documentElement.scrollHeight - window.innerHeight;
    progressBar.style.width = (window.scrollY / h) * 100 + '%';
}, { passive: true });

// ── Cursor Glow ───────────────────────────
const cursorGlow = document.getElementById('cursorGlow');
let glowX = 0,
    glowY = 0,
    targetX = 0,
    targetY = 0;

document.addEventListener('mousemove', e => {
    targetX = e.clientX;
    targetY = e.clientY;
});

function animateGlow() {
    glowX += (targetX - glowX) * 0.12;
    glowY += (targetY - glowY) * 0.12;
    cursorGlow.style.left = glowX + 'px';
    cursorGlow.style.top = glowY + 'px';
    requestAnimationFrame(animateGlow);
}
animateGlow();

// ── Magnetic Buttons ──────────────────────
document.querySelectorAll('.magnetic').forEach(btn => {
    btn.addEventListener('mousemove', e => {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        gsap.to(btn, {
            x: x * 0.3,
            y: y * 0.3,
            duration: 0.4,
            ease: 'power2.out'
        });
    });

    btn.addEventListener('mouseleave', () => {
        gsap.to(btn, {
            x: 0,
            y: 0,
            duration: 0.6,
            ease: 'elastic.out(1, 0.5)'
        });
    });
});

// ── GSAP Hero Entrance ────────────────────
const heroTl = gsap.timeline({ delay: 0.3 });

heroTl.from('.logo', {
        y: -30,
        opacity: 0,
        duration: 0.8,
        ease: 'power3.out'
    })
    .from('.nav-link', {
        y: -20,
        opacity: 0,
        stagger: 0.08,
        duration: 0.6,
        ease: 'power3.out'
    }, '-=0.4');

// ── GSAP Parallax on Floating Icons ───────
document.querySelectorAll('.float-icon[data-speed]').forEach(icon => {
    const speed = parseFloat(icon.dataset.speed) || 1;
    gsap.to(icon, {
        y: -60 * speed,
        ease: 'none',
        scrollTrigger: {
            trigger: '.hero',
            start: 'top top',
            end: 'bottom top',
            scrub: 1
        }
    });
});

// ── GSAP Parallax on Avatar ───────────────
gsap.to('.avatar-frame', {
    y: 40,
    ease: 'none',
    scrollTrigger: {
        trigger: '.hero',
        start: 'top top',
        end: 'bottom top',
        scrub: 1.5
    }
});

// ── Counter Animation (Stats) ─────────────
document.querySelectorAll('.stat-num[data-count]').forEach(el => {
    const target = parseInt(el.dataset.count);
    ScrollTrigger.create({
        trigger: el,
        start: 'top 85%',
        once: true,
        onEnter: () => {
            gsap.to({ val: 0 }, {
                val: target,
                duration: 1.5,
                ease: 'power2.out',
                onUpdate: function() {
                    el.textContent = Math.round(this.targets()[0].val);
                }
            });
        }
    });
});

// ── Skill Bar Animation (GSAP) ────────────
document.querySelectorAll('.skill-fill').forEach(bar => {
    const level = bar.dataset.level;
    ScrollTrigger.create({
        trigger: bar,
        start: 'top 90%',
        once: true,
        onEnter: () => {
            gsap.to(bar, {
                width: level + '%',
                duration: 1.2,
                ease: 'power3.out'
            });
        }
    });
});

// ── Card 3D Tilt ──────────────────────────
document.querySelectorAll('.project-card, .skill-card').forEach(card => {
    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        gsap.to(card, {
            rotateY: x * 10,
            rotateX: -y * 10,
            duration: 0.4,
            ease: 'power2.out',
            transformPerspective: 800
        });
    });

    card.addEventListener('mouseleave', () => {
        gsap.to(card, {
            rotateY: 0,
            rotateX: 0,
            duration: 0.6,
            ease: 'power2.out'
        });
    });
});

// ── Timeline line draw (non-conflicting) ─
const timelineLine = document.querySelector('.timeline::before');
if (timelineLine) {
    gsap.from(timelineLine, {
        scaleY: 0,
        transformOrigin: 'top',
        duration: 1.5,
        ease: 'power2.out',
        scrollTrigger: {
            trigger: '.timeline',
            start: 'top 80%',
            once: true
        }
    });
}

// ── GSAP Section Parallax ─────────────────
gsap.utils.toArray('.section').forEach(section => {
    const inner = section.querySelector('.section-inner');
    if (inner) {
        gsap.from(inner, {
            y: 30,
            ease: 'none',
            scrollTrigger: {
                trigger: section,
                start: 'top bottom',
                end: 'top 60%',
                scrub: 1
            }
        });
    }
});

// ── Particle Canvas ───────────────────────
const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
let particles = [];
let mouse = { x: null, y: null };

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

document.addEventListener('mousemove', e => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
});

class Particle {
    constructor() { this.reset(); }
    reset() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 2 + 0.5;
        this.speedX = (Math.random() - 0.5) * 0.35;
        this.speedY = (Math.random() - 0.5) * 0.35;
        this.opacity = Math.random() * 0.35 + 0.1;
    }
    update() {
        this.x += this.speedX;
        this.y += this.speedY;
        if (mouse.x !== null) {
            const dx = mouse.x - this.x;
            const dy = mouse.y - this.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 130) {
                this.x -= dx * 0.01;
                this.y -= dy * 0.01;
            }
        }
        if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
        if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
    }
    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(108, 140, 255, ${this.opacity})`;
        ctx.fill();
    }
}

const particleCount = Math.min(70, Math.floor(window.innerWidth * 0.05));
for (let i = 0; i < particleCount; i++) particles.push(new Particle());

function connectParticles() {
    for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 130) {
                ctx.beginPath();
                ctx.strokeStyle = `rgba(108, 140, 255, ${0.05 * (1 - dist / 130)})`;
                ctx.lineWidth = 0.5;
                ctx.moveTo(particles[i].x, particles[i].y);
                ctx.lineTo(particles[j].x, particles[j].y);
                ctx.stroke();
            }
        }
    }
}

function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
        p.update();
        p.draw();
    });
    connectParticles();
    requestAnimationFrame(animateParticles);
}
animateParticles();

// ── Active Nav Highlight ──────────────────
const sections = document.querySelectorAll('.section, .hero');
const navLinks = document.querySelectorAll('.nav-link');

const navObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const id = entry.target.id;
            navLinks.forEach(link => {
                link.classList.toggle('active', link.getAttribute('href') === '#' + id);
            });
        }
    });
}, { threshold: 0.3 });

sections.forEach(sec => { if (sec.id) navObserver.observe(sec); });

// ── Smooth Scroll ─────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
        const target = document.querySelector(link.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// ── Contact Form Submission ────────────────
const contactForm = document.getElementById('contactForm');
const submitBtn = document.getElementById('submitBtn');
const submitText = document.getElementById('submitText');
const toast = document.getElementById('toast');
const toastIcon = document.getElementById('toastIcon');
const toastMessage = document.getElementById('toastMessage');

function showToast(message, isSuccess = true) {
    toastMessage.textContent = message;
    toastIcon.textContent = isSuccess ? '✓' : '✗';
    toastIcon.style.color = isSuccess ? '#22c55e' : '#ef4444';

    toast.classList.add('show');

    setTimeout(() => {
        toast.classList.remove('show');
    }, 3500);
}

contactForm.addEventListener('submit', async(e) => {
    e.preventDefault();

    const formData = new FormData(contactForm);
    const data = Object.fromEntries(formData);

    submitBtn.disabled = true;
    submitText.textContent = 'Sending...';

    try {
        const res = await fetch("https://formsubmit.co/ajax/sohebakhtar2001@gmail.com", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (res.ok) {
            showToast('Message sent successfully!', true);
            contactForm.reset();
        } else {
            showToast('Something went wrong. Please try again.', false);
        }
    } catch (error) {
        showToast('Failed to send message. Please try again.', false);
    } finally {
        submitBtn.disabled = false;
        submitText.textContent = 'Send Message';
    }
});