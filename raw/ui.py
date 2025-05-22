import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="✨",
    layout="wide",
)

# Custom CSS for aesthetic improvements
st.markdown("""
<style>
    /* Main text and background colors */
    .main {
        background-color: #f8f9fa;
        color: #1e1e1e;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #3a506b;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Profile image styling */
    .profile-img {
        border-radius: 50%;
        border: 3px solid #5e60ce;
        width: 200px;
        height: 200px;
        object-fit: cover;
        margin-bottom: 20px;
    }
    
    /* Cards for projects */
    .card {
        border-radius: 10px;
        padding: 1.5rem;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
    }
    
    /* Skills progress bars */
    .skill-bar {
        height: 10px;
        border-radius: 5px;
        background-color: #e9ecef;
        margin-bottom: 1rem;
    }
    
    .skill-progress {
        height: 100%;
        border-radius: 5px;
        background-image: linear-gradient(45deg, #6c63ff, #5e60ce);
    }
    
    /* Timeline for experience */
    .timeline-item {
        padding-left: 2rem;
        border-left: 2px solid #6c63ff;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .timeline-dot {
        position: absolute;
        left: -10px;
        top: 0;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: #6c63ff;
    }
    
    /* Contact form styling */
    .contact-form {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Custom option menu styling */
    .css-1cypcdb {
        background-color: #6c63ff !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #6c757d;
        font-size: 0.9rem;
    }

    /* Social icons */
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .social-icon {
        font-size: 1.5rem;
        color: #6c63ff;
        transition: transform 0.3s ease;
    }
    
    .social-icon:hover {
        transform: scale(1.2);
    }
</style>
""", unsafe_allow_html=True)

# Navigation with streamlit-option-menu
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Projects", "Skills", "Experience", "Contact"],
        icons=["house", "person", "code-slash", "graph-up", "clock-history", "envelope"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#6c63ff", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#6c63ff", "color": "white"},
        },
    )


# Home Section
if selected == "Home":
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
            <h1 style="font-size: 3rem; margin-bottom: 1rem;">Hello, I'm <span style="color: #6c63ff;">Your Name</span></h1>
            <h2 style="font-size: 2rem; margin-bottom: 2rem; color: #6c757d;">Frontend Developer & UI/UX Designer</h2>
            <p style="font-size: 1.2rem; margin-bottom: 2rem; color: #6c757d;">
                Passionate about creating beautiful, functional, and user-friendly applications.
                Let's bring your ideas to life!
            </p>
            <div>
                <button style="background-color: #6c63ff; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 5px; font-size: 1rem; cursor: pointer; margin-right: 1rem;">Download CV</button>
                <button style="background-color: transparent; color: #6c63ff; border: 2px solid #6c63ff; padding: 0.75rem 1.5rem; border-radius: 5px; font-size: 1rem; cursor: pointer;">Contact Me</button>
            </div>
            <div class="social-icons">
                <span class="social-icon">📱</span>
                <span class="social-icon">💼</span>
                <span class="social-icon">🐦</span>
                <span class="social-icon">📸</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="https://source.unsplash.com/300x300/?portrait" class="profile-img" style="width: 300px; height: 300px;">
        </div>
        """, unsafe_allow_html=True)

# About Section
elif selected == "About":
    st.markdown("<h1>About Me</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <img src="https://source.unsplash.com/400x500/?portrait" style="width: 100%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <h2>Who am I?</h2>
        <p style="font-size: 1.1rem; line-height: 1.7;">
            I'm a passionate frontend developer and UI/UX designer with over 5 years of experience creating beautiful, 
            functional, and user-friendly applications. I focus on creating clean code and intuitive designs that provide 
            exceptional user experiences.
        </p>
        
        <h3>Personal Info</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div>
                <p><strong>Name:</strong> Your Name</p>
                <p><strong>Age:</strong> 28</p>
                <p><strong>Location:</strong> San Francisco, CA</p>
                <p><strong>Experience:</strong> 5+ Years</p>
            </div>
            <div>
                <p><strong>Email:</strong> your.email@example.com</p>
                <p><strong>Phone:</strong> +1 (123) 456-7890</p>
                <p><strong>Freelance:</strong> Available</p>
                <p><strong>Languages:</strong> English, Spanish</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Education and Certifications
    st.markdown("<h2>Education & Certifications</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Master of Computer Science</h3>
            <p>Stanford University</p>
            <p>2018 - 2020</p>
        </div>
        <div class="card">
            <h3>Bachelor of Design</h3>
            <p>Rhode Island School of Design</p>
            <p>2014 - 2018</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Google UX Design Professional Certificate</h3>
            <p>Google</p>
            <p>2021</p>
        </div>
        <div class="card">
            <h3>Full Stack Web Development</h3>
            <p>Udacity</p>
            <p>2019</p>
        </div>
        """, unsafe_allow_html=True)

# Projects Section
elif selected == "Projects":
    st.markdown("<h1>My Projects</h1>", unsafe_allow_html=True)
    
    # Filter by category
    categories = ["All", "Web Development", "UI/UX Design", "Mobile Apps", "Data Visualization"]
    selected_category = st.selectbox("Filter by category", categories)
    
    # Project cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <img src="https://source.unsplash.com/700x400/?website" style="width: 100%; border-radius: 5px; margin-bottom: 1rem;">
            <h3>E-commerce Website</h3>
            <p style="color: #6c63ff;">Web Development</p>
            <p>A fully responsive e-commerce website built with React, Node.js, and MongoDB. Features include user authentication, product filtering, shopping cart, and payment integration.</p>
            <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">React</span>
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">Node.js</span>
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">MongoDB</span>
            </div>
            <button style="background-color: #6c63ff; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px; font-size: 0.9rem; cursor: pointer; margin-top: 1rem;">View Project</button>
        </div>
        
        <div class="card">
            <img src="https://source.unsplash.com/700x400/?dashboard" style="width: 100%; border-radius: 5px; margin-bottom: 1rem;">
            <h3>Analytics Dashboard</h3>
            <p style="color: #6c63ff;">Data Visualization</p>
            <p>An interactive dashboard for visualizing business metrics and KPIs. Built with D3.js and React, featuring real-time updates and customizable views.</p>
            <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">D3.js</span>
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">React</span>
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">Firebase</span>
            </div>
            <button style="background-color: #6c63ff; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px; font-size: 0.9rem; cursor: pointer; margin-top: 1rem;">View Project</button>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <img src="https://source.unsplash.com/700x400/?mobile-app" style="width: 100%; border-radius: 5px; margin-bottom: 1rem;">
            <h3>Fitness Tracker App</h3>
            <p style="color: #6c63ff;">Mobile Apps</p>
            <p>A cross-platform mobile app for tracking workouts, nutrition, and health metrics. Built with React Native and integrated with health APIs.</p>
            <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">React Native</span>
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">Redux</span>
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">GraphQL</span>
            </div>
            <button style="background-color: #6c63ff; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px; font-size: 0.9rem; cursor: pointer; margin-top: 1rem;">View Project</button>
        </div>
        
        <div class="card">
            <img src="https://source.unsplash.com/700x400/?design" style="width: 100%; border-radius: 5px; margin-bottom: 1rem;">
            <h3>Travel App UI Design</h3>
            <p style="color: #6c63ff;">UI/UX Design</p>
            <p>A comprehensive UI/UX design for a travel booking app. Includes user research, wireframes, prototypes, and a complete design system.</p>
            <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">Figma</span>
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">Adobe XD</span>
                <span style="background-color: #f8f9fa; padding: 0.25rem 0.5rem; border-radius: 5px; font-size: 0.8rem;">Prototyping</span>
            </div>
            <button style="background-color: #6c63ff; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px; font-size: 0.9rem; cursor: pointer; margin-top: 1rem;">View Project</button>
        </div>
        """, unsafe_allow_html=True)

# Skills Section
elif selected == "Skills":
    st.markdown("<h1>My Skills</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Technical Skills
    with col1:
        st.markdown("<h2>Technical Skills</h2>", unsafe_allow_html=True)
        
        skills = {
            "HTML/CSS": 95,
            "JavaScript": 90,
            "React": 85,
            "Node.js": 75,
            "Python": 80,
            "UI/UX Design": 90,
            "SQL": 70,
            "AWS": 65
        }
        
        for skill, proficiency in skills.items():
            st.markdown(f"""
            <div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>{skill}</span>
                    <span>{proficiency}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {proficiency}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Soft Skills with Radar Chart
    with col2:
        st.markdown("<h2>Soft Skills</h2>", unsafe_allow_html=True)
        
        soft_skills = {
            'Communication': 90,
            'Leadership': 85,
            'Problem Solving': 95,
            'Teamwork': 90,
            'Creativity': 85,
            'Time Management': 80
        }
        
        df = pd.DataFrame({
            'Skill': list(soft_skills.keys()),
            'Value': list(soft_skills.values())
        })
        
        fig = px.line_polar(
            df, r='Value', theta='Skill', line_close=True,
            range_r=[0, 100],
            color_discrete_sequence=['#6c63ff']
        )
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#3a506b'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Tools & Technologies
    st.markdown("<h2>Tools & Technologies</h2>", unsafe_allow_html=True)
    
    # Display tools as icons or logos
    col1, col2, col3, col4, col5 = st.columns(5)
    
    tools = [
        {"name": "VS Code", "icon": "💻"},
        {"name": "Figma", "icon": "🎨"},
        {"name": "Git", "icon": "🔄"},
        {"name": "Docker", "icon": "🐳"},
        {"name": "AWS", "icon": "☁️"},
        {"name": "Adobe XD", "icon": "✏️"},
        {"name": "Photoshop", "icon": "🖌️"},
        {"name": "Notion", "icon": "📝"},
        {"name": "Slack", "icon": "💬"},
        {"name": "Jira", "icon": "📊"}
    ]
    
    cols = [col1, col2, col3, col4, col5]
    
    for i, tool in enumerate(tools):
        col_idx = i % 5
        cols[col_idx].markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 1.5rem;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{tool['icon']}</div>
            <div style="text-align: center;">{tool['name']}</div>
        </div>
        """, unsafe_allow_html=True)

# Experience Section
elif selected == "Experience":
    st.markdown("<h1>My Experience</h1>", unsafe_allow_html=True)
    
    # Experience timeline
    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <h3>Senior Frontend Developer</h3>
        <p style="color: #6c63ff;">Google - 2022 to Present</p>
        <p>
            Led a team of developers in creating responsive web applications using React and TypeScript.
            Implemented CI/CD pipelines and improved performance by 40%. Collaborated with UX designers 
            to implement design systems and component libraries.
        </p>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <h3>UI/UX Designer</h3>
        <p style="color: #6c63ff;">Apple - 2020 to 2022</p>
        <p>
            Designed user interfaces for mobile applications with a focus on accessibility and user experience.
            Created wireframes, prototypes, and design systems. Conducted user research and usability testing
            to improve product designs.
        </p>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <h3>Frontend Developer</h3>
        <p style="color: #6c63ff;">Netflix - 2018 to 2020</p>
        <p>
            Developed and maintained frontend components for the streaming platform using React and Redux.
            Optimized application performance and implemented responsive designs. Collaborated with backend
            developers to integrate APIs.
        </p>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <h3>Web Developer Intern</h3>
        <p style="color: #6c63ff;">Adobe - 2017 to 2018</p>
        <p>
            Assisted in developing web applications and implementing UI designs. Learned modern frontend
            technologies and best practices. Participated in code reviews and agile development processes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key achievements
    st.markdown("<h2>Key Achievements</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background-color: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h1 style="font-size: 3rem; color: #6c63ff; margin-bottom: 1rem;">50+</h1>
            <p style="font-size: 1.2rem;">Projects Completed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background-color: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h1 style="font-size: 3rem; color: #6c63ff; margin-bottom: 1rem;">30+</h1>
            <p style="font-size: 1.2rem;">Happy Clients</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background-color: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h1 style="font-size: 3rem; color: #6c63ff; margin-bottom: 1rem;">5+</h1>
            <p style="font-size: 1.2rem;">Years Experience</p>
        </div>
        """, unsafe_allow_html=True)

# Contact Section
elif selected == "Contact":
    st.markdown("<h1>Get In Touch</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-form">
            <h2>Send A Message</h2>
            <p style="margin-bottom: 2rem;">Feel free to contact me for any work or collaboration opportunities.</p>
        """, unsafe_allow_html=True)
        
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")
        
        if st.button("Send Message", key="send_message"):
            st.success("Message sent successfully! I'll get back to you soon.")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h2>Contact Information</h2>
            
            <div style="margin-top: 1.5rem;">
                <p style="font-weight: bold; margin-bottom: 0.5rem;">Email:</p>
                <p>your.email@example.com</p>
            </div>
            
            <div style="margin-top: 1.5rem;">
                <p style="font-weight: bold; margin-bottom: 0.5rem;">Phone:</p>
                <p>+1 (123) 456-7890</p>
            </div>
            
            <div style="margin-top: 1.5rem;">
                <p style="font-weight: bold; margin-bottom: 0.5rem;">Address:</p>
                <p>San Francisco, CA</p>
            </div>
            
            <div class="social-icons" style="margin-top: 2rem;">
                <span class="social-icon">📱</span>
                <span class="social-icon">💼</span>
                <span class="social-icon">🐦</span>
                <span class="social-icon">📸</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 Your Name. All rights reserved.</p>
    <p>Designed with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)