import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Experience -> Education
experience_regex = re.compile(r'<!-- Experience -->\s*<section id="experience" class="section">.*?</section>', re.DOTALL)
new_experience = """<!-- Experience -->
  <section id="experience" class="section">
    <div class="section-inner">
      <h2 class="section-title" data-aos="fade-up">Education</h2>

      <div class="timeline">
        <div class="timeline-item" data-aos="fade-up" style="--delay:.1s">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <span class="timeline-date">2021 – 2025</span>
            <h3>Bachelor of Technology in Computer Science</h3>
            <p><strong>Jaypee University Of Engineering And Technology</strong> Guna, MP</p>
          </div>
        </div>
        <div class="timeline-item" data-aos="fade-up" style="--delay:.2s">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <span class="timeline-date">2019 – 2020</span>
            <h3>Intermediate</h3>
            <p><strong>Maheshwari Academy Secondary School</strong> Katihar, Bihar</p>
          </div>
        </div>
        <div class="timeline-item" data-aos="fade-up" style="--delay:.3s">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <span class="timeline-date">2017 – 2018</span>
            <h3>High School</h3>
            <p><strong>Maheshwari Academy Secondary School</strong> Katihar, Bihar</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""
html = experience_regex.sub(new_experience, html)

# 2. Skills
skills_regex = re.compile(r'<!-- Programming Languages -->\s*<h3 class="skills-category" data-aos="fade-up">Programming Languages</h3>.*?</div>\s*</div>\s*</section>', re.DOTALL)
new_skills = """<!-- Programming Languages -->
      <h3 class="skills-category" data-aos="fade-up">Programming Languages & Frontend</h3>
      <div class="skills-grid">
        <div class="skill-card" data-aos="fade-up" style="--delay:.1s">
          <div class="skill-icon">C++</div>
          <h3>C++</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="85"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.15s">
          <div class="skill-icon">☕</div>
          <h3>Java</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="80"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.2s">
          <div class="skill-icon">SQL</div>
          <h3>SQL</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="85"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.25s">
          <div class="skill-icon">JS</div>
          <h3>JavaScript</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="90"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.3s">
          <div class="skill-icon">⚛️</div>
          <h3>React</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="85"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.35s">
          <div class="skill-icon">🌐</div>
          <h3>HTML / CSS</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="95"></div></div>
        </div>
      </div>

      <!-- Tools & Technologies -->
      <h3 class="skills-category" data-aos="fade-up">Tools & Technologies</h3>
      <div class="skills-grid">
        <div class="skill-card" data-aos="fade-up" style="--delay:.1s">
          <div class="skill-icon">💻</div>
          <h3>VS Code</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="90"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.15s">
          <div class="skill-icon">⚙️</div>
          <h3>GitHub</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="85"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.2s">
          <div class="skill-icon">🍃</div>
          <h3>MongoDB</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="80"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.25s">
          <div class="skill-icon">🗄️</div>
          <h3>MySQL</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="85"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.3s">
          <div class="skill-icon">🧪</div>
          <h3>Postman</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="80"></div></div>
        </div>
      </div>

      <!-- CS Fundamentals -->
      <h3 class="skills-category" data-aos="fade-up">CS Fundamentals</h3>
      <div class="skills-grid">
        <div class="skill-card" data-aos="fade-up" style="--delay:.1s">
          <div class="skill-icon">🧠</div>
          <h3>OOPs</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="85"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.15s">
          <div class="skill-icon">🗃️</div>
          <h3>DBMS</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="85"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.2s">
          <div class="skill-icon">📊</div>
          <h3>Data Structures</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="90"></div></div>
        </div>
        <div class="skill-card" data-aos="fade-up" style="--delay:.25s">
          <div class="skill-icon">📈</div>
          <h3>Algorithms</h3>
          <div class="skill-bar"><div class="skill-fill" data-level="85"></div></div>
        </div>
      </div>
    </div>
  </section>"""
html = skills_regex.sub(new_skills, html)

# 3. Projects
projects_regex = re.compile(r'<div class="project-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
new_projects = """<div class="project-grid">
        <div class="project-card" data-aos="fade-up" style="--delay:.1s">
          <div class="project-card-header">
            <div class="project-icon">🛒</div>
          </div>
          <h3>E-Commerce Website Full Stack</h3>
          <p>Designed and developed a full-stack e-commerce platform managing over 10,000+ product entries.</p>
          <div class="project-tags">
            <span>React.js</span><span>Node.js</span><span>Express.js</span><span>MongoDB</span>
          </div>
          <button class="work-upon-btn" onclick="this.closest('.project-card').classList.toggle('expanded')">
            Work Upon <span class="work-upon-arrow">▾</span>
          </button>
          <div class="work-upon-panel">
            <ul>
              <li><strong>Scale:</strong> Manged 10,000+ product entries successfully.</li>
              <li><strong>Features:</strong> Product browsing, advanced filtering, cart management, and secure credit card transaction integration.</li>
              <li><strong>Dashboard:</strong> Built an admin dashboard to manage 100+ categories and track product status updates.</li>
            </ul>
          </div>
        </div>

        <div class="project-card" data-aos="fade-up" style="--delay:.2s">
          <div class="project-card-header">
            <div class="project-icon">🚀</div>
          </div>
          <h3>Space Research Website Frontend</h3>
          <p>Crafted a visually appealing website showcasing the latest developments in space research.</p>
          <div class="project-tags">
            <span>HTML</span><span>CSS</span><span>JavaScript</span>
          </div>
          <button class="work-upon-btn" onclick="this.closest('.project-card').classList.toggle('expanded')">
            Work Upon <span class="work-upon-arrow">▾</span>
          </button>
          <div class="work-upon-panel">
            <ul>
              <li><strong>Engagement:</strong> Achieved 95% user satisfaction with dynamic visuals and animations.</li>
              <li><strong>Navigation:</strong> Seamlessly enabled users to explore 10+ missions and 20+ research highlights effortlessly.</li>
              <li><strong>UX:</strong> Executed 5+ interactive elements for maximizing visitor engagement.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>"""
html = projects_regex.sub(new_projects, html)

# 4. Achievements
achievements_regex = re.compile(r'<!-- Achievements -->\s*<section id="achievements" class="section">.*?</section>', re.DOTALL)
new_achievements = """<!-- Achievements -->
  <section id="achievements" class="section">
    <div class="section-inner">
      <h2 class="section-title" data-aos="fade-up">Key <span class="gradient-text">Achievements</span></h2>
      <p class="section-sub" data-aos="fade-up" data-aos-delay="100">Competitive programming and extracurricular milestones</p>

      <div class="timeline">
        <div class="timeline-item" data-aos="fade-up" style="--delay:.1s">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <h3>LeetCode</h3>
            <p>Solved <strong>400+ problems</strong> on LeetCode, continually strengthening Data Structures and Algorithms proficiency.</p>
          </div>
        </div>

        <div class="timeline-item" data-aos="fade-up" style="--delay:.2s">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <h3>Badminton Tournaments</h3>
            <p>&bull; Participated in over <strong>5+ competitive badminton tournaments</strong>, competing against players from various skill levels.<br><br>
            &bull; Secured victory in <strong>3 championships</strong>, showcasing strong strategy, precision, and teamwork.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""
html = achievements_regex.sub(new_achievements, html)

# 5. Certifications
certifications_regex = re.compile(r'<!-- Certifications -->\s*<section id="certifications" class="section">.*?</section>', re.DOTALL)
new_certifications = """<!-- Certifications -->
  <section id="certifications" class="section">
    <div class="section-inner">
      <h2 class="section-title" data-aos="fade-up">My <span class="gradient-text">Certifications</span></h2>

      <div class="certifications-grid">
        <div class="certification-card" data-aos="fade-up" style="--delay:.1s">
          <div class="cert-icon">📜</div>
          <h3>Mastering Data Structures & Algorithms</h3>
        </div>
        <div class="certification-card" data-aos="fade-up" style="--delay:.2s">
          <div class="cert-icon">📜</div>
          <h3>C++ Programming for Beginners</h3>
        </div>
        <div class="certification-card" data-aos="fade-up" style="--delay:.3s">
          <div class="cert-icon">📜</div>
          <h3>Java Programming for Beginners</h3>
        </div>
        <div class="certification-card" data-aos="fade-up" style="--delay:.4s">
          <div class="cert-icon">📜</div>
          <h3>HTML CSS and JavaScript for Beginners</h3>
        </div>
      </div>
    </div>
  </section>"""
html = certifications_regex.sub(new_certifications, html)

# 6. Contact
contact_regex = re.compile(r'<div class="contact-info" data-aos="fade-up" data-aos-delay="200">.*?</div>\s*</div>\s*</section>', re.DOTALL)
new_contact = """<div class="contact-info" data-aos="fade-up" data-aos-delay="200">
          <div class="contact-item">
            <span class="contact-icon">📍</span>
            <div><strong>Location</strong>
              <p>Katihar, Bihar, 854117</p>
            </div>
          </div>
          
          <div class="contact-item">
            <span class="contact-icon">📱</span>
            <div><strong>Phone</strong>
              <p>+91 9693039834</p>
            </div>
          </div>
          
          <div class="contact-item">
            <span class="contact-icon">📧</span>
            <div><strong>Email</strong>
              <p>sohebakhtar2001@gmail.com</p>
            </div>
          </div>

          <div class="social-links">
            <a href="#" target="_blank" rel="noreferrer"
              class="social-btn" title="LinkedIn">in</a>
            <a href="#" target="_blank" rel="noreferrer" class="social-btn"
              title="GitHub">GH</a>
          </div>
        </div>
      </div>
    </div>
  </section>"""
html = contact_regex.sub(new_contact, html)

# 7. Footer
footer_regex = re.compile(r'<p>© <span id="year"></span> Soheb Akhtar — Crafted with care</p>')
html = footer_regex.sub(r'<p>© <span id="year"></span> Soheb Akhtar — Crafted with care</p>', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
