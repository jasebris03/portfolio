// Mobile navigation functionality
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
}));

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar background on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = 'none';
    }
});

// Load and display portfolio data
async function loadPortfolioData() {
    try {
        const response = await fetch('portfolio_data.json');
        const data = await response.json();
        
        // Update hero section
        updateHeroSection(data.personal_info);
        
        // Update about section
        updateAboutSection(data.personal_info);
        
        // Update skills section
        updateSkillsSection(data.personal_info.skills);
        
        // Update experience section
        updateExperienceSection(data.personal_info.experience);
        
        // Update contact section
        updateContactSection(data.personal_info.contact);
        
    } catch (error) {
        console.error('Error loading portfolio data:', error);
    }
}

function updateHeroSection(personalInfo) {
    const heroName = document.getElementById('hero-name');
    const heroTitle = document.getElementById('hero-title');
    const heroSummary = document.getElementById('hero-summary');
    
    if (heroName && personalInfo.name) {
        heroName.textContent = personalInfo.name;
    }
    
    if (heroTitle && personalInfo.title) {
        heroTitle.textContent = personalInfo.title;
    }
    
    if (heroSummary && personalInfo.summary) {
        heroSummary.textContent = personalInfo.summary;
    }
}

function updateAboutSection(personalInfo) {
    const aboutSummary = document.getElementById('about-summary');
    
    if (aboutSummary && personalInfo.summary) {
        // Use the summary from CV but keep it conversational
        aboutSummary.textContent = personalInfo.summary;
    }
}

function updateSkillsSection(skills) {
    if (!skills || skills.length === 0) return;
    
    // Categorize skills
    const infrastructureSkills = ['AWS', 'Azure', 'Terraform', 'CDK', 'CloudFormation', 'Docker', 'Kubernetes', 'ECS', 'EKS', 'Helm', 'Lambda', 'Step Functions', 'API Gateway'];
    const programmingSkills = ['Python', 'Node JS', 'Bash', 'FastAPI', 'SQLAlchemy'];
    const toolsSkills = ['GitHub Actions', 'BitBucket Pipelines', 'AWS CodePipeline', 'Sentry', 'CloudWatch', 'X-Ray', 'OTEL', 'Hashicorp Vault', 'Snyk'];
    
    const infrastructureContainer = document.getElementById('infrastructure-skills');
    const programmingContainer = document.getElementById('programming-skills');
    const toolsContainer = document.getElementById('tools-skills');
    
    skills.forEach(skill => {
        const skillTag = document.createElement('span');
        skillTag.className = 'skill-tag';
        skillTag.textContent = skill;
        
        if (infrastructureSkills.some(s => skill.toLowerCase().includes(s.toLowerCase()))) {
            infrastructureContainer.appendChild(skillTag);
        } else if (programmingSkills.some(s => skill.toLowerCase().includes(s.toLowerCase()))) {
            programmingContainer.appendChild(skillTag);
        } else {
            toolsContainer.appendChild(skillTag);
        }
    });
}

function updateExperienceSection(experience) {
    const experienceGrid = document.getElementById('experience-grid');
    
    if (!experience || experience.length === 0) {
        experienceGrid.innerHTML = `
            <div class="experience-card" style="grid-column: 1 / -1; text-align: center;">
                <h3>Experience information coming soon!</h3>
            </div>
        `;
        return;
    }
    
    experience.forEach(job => {
        const experienceCard = createExperienceCard(job);
        experienceGrid.appendChild(experienceCard);
    });
}

function createExperienceCard(job) {
    const card = document.createElement('div');
    card.className = 'experience-card';
    
    const responsibilities = job.responsibilities ? job.responsibilities.map(resp => `<li>${resp}</li>`).join('') : '';
    
    card.innerHTML = `
        <div class="experience-header">
            <div>
                <h3 class="experience-title">${job.title}</h3>
                <p class="experience-company">${job.company}</p>
            </div>
            <div class="experience-meta">
                <span class="experience-location">${job.location}</span>
                <span class="experience-date">${job.date}</span>
            </div>
        </div>
        <div class="experience-content">
            <ul class="experience-responsibilities">
                ${responsibilities}
            </ul>
        </div>
    `;
    
    return card;
}

function updateContactSection(contact) {
    const contactEmail = document.getElementById('contact-email');
    const contactPhone = document.getElementById('contact-phone');
    const contactLocation = document.getElementById('contact-location');
    
    if (contactEmail && contact.email) {
        contactEmail.textContent = contact.email;
    }
    
    if (contactPhone && contact.phone) {
        contactPhone.textContent = contact.phone;
    }
    
    if (contactLocation && contact.location) {
        contactLocation.textContent = contact.location;
    }
}



// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    loadPortfolioData();
    
    // Add fun easter egg to logo
    const logo = document.querySelector('.logo-text');
    let clickCount = 0;
    const funMessages = [
        "🚀 Deploying...",
        "⚡ Powering up...",
        "🐳 Containerizing...",
        "☁️ Cloud computing...",
        "🔧 Infrastructure as Code!"
    ];
    
    logo.addEventListener('click', () => {
        clickCount++;
        const originalText = logo.textContent;
        const message = funMessages[clickCount % funMessages.length];
        
        logo.textContent = message;
        logo.style.transform = 'scale(1.1)';
        
        setTimeout(() => {
            logo.textContent = originalText;
            logo.style.transform = 'scale(1)';
        }, 1000);
    });
});

console.log(`
🚀 Welcome to Jason's Portfolio!
⚡ Built with modern web technologies
🐳 Containerized with love
☁️ Ready for cloud deployment
🔧 Infrastructure as Code enthusiast

Thanks for checking out my work! 👨‍💻
`); 