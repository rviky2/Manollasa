from django.shortcuts import render
from django.views import View
from core.models import course


def PageNotFound(request, something):
    return render(request, 'pagenotfound.html')


class UniversityTemplateView(View):
    

    def get(self, request, template_name):
        # Check if the requested template name exists in the templates dictionary
        template = 'sikkim.html'

        if template:
            return render(request, template)
        else:
            # Handle cases where the template name is not found
            return render(request, 'pagenotfound.html')


class ConsultancyTemplateView(View):
    data = {
        'pharmacy': {
            'title': 'Manollasa Pharmacy',
            'keyword': 'pharm',
            'content': '''
   <h3>Manollasa Pharmacy: Your Trusted Health Partner</h3>

At Manollasa Pharmacy, we are committed to providing reliable and accessible healthcare solutions to our community. Our pharmacy offers a wide range of medications, health products, and professional services to cater to your health and wellness needs.
   <br><br> <h2>Services We Provide</h2>

    <ul>
        <li><strong>Medication Dispensing:</strong> Access to a comprehensive range of prescription and over-the-counter medications.</li>

        <li><strong>Health Products:</strong> Various health and wellness products including vitamins, supplements, and personal care items.</li>

        <li><strong>Consultation Services:</strong> Expert advice and consultation from licensed pharmacists to address your healthcare queries and concerns.</li>

        <li><strong>Health Monitoring Devices:</strong> Availability of devices for health monitoring such as blood pressure monitors, glucose meters, and more.</li>

        <li><strong>Home Delivery:</strong> Convenient home delivery services for your medications and healthcare essentials.</li>
    </ul>

    <h2>Why Choose Manollasa Pharmacy</h2>

 Our commitment to quality, reliability, and personalized care sets us apart as your trusted health partner:

    <ul>
        <li><strong>Professional Guidance:</strong> Our experienced pharmacists provide expert guidance and advice for your health needs.</li>

        <li><strong>Convenience:</strong> Convenient access to medications, health products, and consultation services under one roof.</li>

        <li><strong>Community-Centric Approach:</strong> We prioritize the health and well-being of our community, delivering exceptional service with care and empathy.</li>
    </ul>

    <h2>Get in Touch</h2>

   Visit our pharmacy today or contact us to learn more about our services. We are here to assist you in managing your health and well-being.
''',
        },
        'nursing': {
            'title': 'Manollasa Nursing',
            'keyword': 'nursing',
            'content': '''
<h3>Nursing: Compassionate Care and Critical Expertise</h3>

    Nursing stands at the heart of healthcare, embodying both empathy and expertise. It's a profession that blends scientific knowledge with compassionate care, playing a pivotal role in the well-being of individuals and communities.
  <br><br>
    <h2>Role of Nurses</h2>

    Nurses are the frontline heroes, offering round-the-clock care, comfort, and support to patients. They assess, plan, implement, and evaluate patient care, providing a holistic approach to health management.
  <br><br>
    <h2>Key Responsibilities</h2>

    <ul>
        <li><strong>Patient Advocacy:</strong> Nurses serve as advocates for their patients, ensuring their voices are heard and their needs are met within the healthcare system.</li>

        <li><strong>Health Promotion:</strong> They educate and empower individuals and communities to adopt healthy lifestyles and preventive measures.</li>

        <li><strong>Collaboration:</strong> Nurses collaborate with multidisciplinary teams, working alongside doctors, therapists, and other healthcare professionals to provide comprehensive care.</li>
    </ul>

    <h2>Specializations and Diversity</h2>

    The nursing profession offers a spectrum of specializations, from pediatrics to geriatrics, mental health to critical care, and beyond. Each specialization demands unique skills and a deep understanding of...
   

'''},
        'physiotherapy': {
            'title': 'Manollasa Physiotherapy',
            'keyword': 'physiotherapy',
            'content': '''   <h3>Manollasa Physiotherapy: Restoring Health, Enhancing Movement</h3>

    At Manollasa Physiotherapy, we are dedicated to restoring mobility and improving the quality of life for our patients. Our approach combines expertise, compassion, and personalized care to address a range of musculoskeletal and neurological conditions.
  <br><br>
    <h2>Our Expert Team</h2>

    Our team of skilled physiotherapists is committed to providing comprehensive assessments and individualized treatment plans to address your specific needs. We believe in a holistic approach to rehabilitation, focusing on both recovery and prevention.
  <br><br>
    <h2>Key Services</h2>

    <ul>
        <li><strong>Rehabilitation Programs:</strong> Tailored programs designed to restore function, reduce pain, and enhance mobility following injuries or surgeries.</li>

        <li><strong>Manual Therapy:</strong> Hands-on techniques to alleviate pain, improve joint mobility, and promote healing.</li>

        <li><strong>Exercise Prescription:</strong> Customized exercise plans to strengthen muscles, improve flexibility, and prevent re-injury.</li>

        <li><strong>Specialized Treatments:</strong> Advanced modalities such as electrotherapy or ultrasound to aid in healing and recovery.</li>
    </ul>

    <h2>Our Approach</h2>

    At Manollasa Physiotherapy, we prioritize patient-centered care. We work collaboratively with our patients, empowering them with the knowledge and tools necessary for their rehabilitation journey.
  <br><br>
    <h2>Positive Impact</h2>

    Our goal is not just to restore movement, but to improve overall well-being. By restoring function and providing ongoing support, we aim to enhance independence and optimize your quality of life.

'''},
        'mahs': {
            'title': 'Manollasa Allied & Health Science',
            'keyword': 'medical',
            'content': '''  <h3>Manollasa Allied and Health Science: Empowering Careers, Advancing Healthcare</h3>

   At Manollasa Allied and Health Science, we are dedicated to shaping the future of healthcare professionals. Our programs offer comprehensive education and hands-on training to prepare individuals for diverse careers in the healthcare industry.

    <h2>Our Programs</h2>

   We offer a range of programs covering various allied and health science disciplines:

    <ul>
        <li><strong>Medical Laboratory Technology:</strong> Training in laboratory procedures and techniques for accurate diagnostic testing.</li>

        <li><strong>Radiologic Technology:</strong> Education on medical imaging techniques and technology used in diagnostic procedures.</li>

        <li><strong>Physical Therapy Assistant:</strong> Training to assist physical therapists in providing rehabilitative services to patients.</li>

        <li><strong>Occupational Therapy Assistant:</strong> Learning skills to assist occupational therapists in providing therapy to individuals with disabilities or injuries.</li>

        <li><strong>Health Information Management:</strong> Education on managing healthcare data, records, and information systems.</li>
    </ul>

    <h2>Our Approach</h2>

   We believe in a practical, hands-on approach to learning. Our programs combine classroom instruction with practical training, providing students with real-world experience to excel in their chosen field.

    <h2>Career Opportunities</h2>

   Our programs prepare students for a wide array of career opportunities in healthcare facilities, laboratories, rehabilitation centers, and more. Graduates are equipped with the skills and knowledge to make a meaningful impact in the healthcare industry.

''',
        },
        'mgc': {
            'title': 'Manollasa Guidance & Counselling',
            'keyword': 'mgc',
            'content': ''' 
 <h3>Manollasa Guidance and Counselling: Nurturing Minds, Empowering Lives</h3>

   At Manollasa Guidance and Counselling, we are committed to providing comprehensive guidance and support to individuals seeking personal development and emotional well-being. Our services aim to foster growth, resilience, and positive mental health.
  <br><br>
    <h2>Our Approach</h2>

   We believe in a client-centered approach, tailoring our guidance and counselling services to meet the unique needs of each individual. Our experienced counsellors provide a safe and supportive environment for self-exploration and growth.
  <br><br>
    <h2>Services We Offer</h2>

   We offer a range of services to address various personal, academic, and emotional needs:

    <ul>
        <li><strong>Individual Counselling:</strong> One-on-one sessions focusing on personal growth, self-awareness, and coping strategies.</li>

        <li><strong>Academic Counselling:</strong> Guidance and support for educational planning, career exploration, and academic success.</li>

        <li><strong>Family Counselling:</strong> Assisting families in resolving conflicts, improving communication, and fostering healthier relationships.</li>

        <li><strong>Stress Management:</strong> Techniques and strategies to manage stress, anxiety, and emotional challenges.</li>

        <li><strong>Life Skills Coaching:</strong> Development of essential life skills such as decision-making, problem-solving, and resilience.</li>
    </ul>

    <h2>Empowering Lives</h2>

   Our aim is to empower individuals to overcome challenges, build resilience, and lead fulfilling lives. Through our guidance and counselling services, we strive to promote mental health and well-being for all.

''',
        },
        'paramedical': {
            'title': 'Manollasa Paramedical',
            'keyword': 'medical',
            'content': ''' 
 <h3>Manollasa Paramedical: Excellence in Healthcare Support</h1>

   At Manollasa Paramedical, we are dedicated to providing essential support services in the healthcare sector. Our paramedical programs equip individuals with the necessary skills and expertise to assist healthcare professionals and contribute to patient care.
  <br><br>
    <h2>Our Programs</h2>

   We offer a range of paramedical programs designed to train individuals for roles supporting various aspects of healthcare:

    <ul>
        <li><strong>Emergency Medical Technician (EMT):</strong> Training individuals in emergency medical care, providing immediate assistance in critical situations.</li>

        <li><strong>Medical Laboratory Technology:</strong> Education on laboratory procedures and diagnostic testing to aid in accurate medical diagnoses.</li>

        <li><strong>Radiologic Technology:</strong> Training in medical imaging techniques to assist in diagnostic procedures.</li>

        <li><strong>Pharmacy Technician:</strong> Preparation to support pharmacists in dispensing medications and providing patient education.</li>

        <li><strong>Healthcare Assistant:</strong> Learning essential caregiving skills to support patients with daily activities and provide compassionate care.</li>
    </ul>

    <h2>Our Commitment</h2>

   Our programs focus on practical training and hands-on experience, preparing individuals to excel in their roles within the healthcare industry. We prioritize quality education and adherence to professional standards.
  <br><br>
    <h2>Career Opportunities</h2>

   Graduates from our paramedical programs are well-equipped to pursue diverse career opportunities in hospitals, clinics, laboratories, and other healthcare settings. They play a crucial role in supporting healthcare teams and improving patient outcomes.

    
''',
        }

    }

    def get(self, request, template_name):
        template = 'consultancy.html'
        data = self.data.get(template_name)
        data['course_objs'] = course.objects.filter(
            name__icontains=data.get('keyword'))
        if template:
            return render(request, template, context=data)
        else:
            return render(request, 'pagenotfound.html')


class FreeServiceTemplateView(View):
    data = {
        'seniorHealth': {
            'content': '''
<h3>Student Helpline: Your Support System, Anytime, Anywhere</h3>

    At Manollasa, we understand the importance of accessible support for students navigating academic challenges and personal hurdles. Our Student Helpline operates round-the-clock, 24 hours a day, 7 days a week, to provide immediate assistance and guidance to students in need.
<br><br>
    <h2>What We Offer</h2>

    <ul>
        <li><strong>Academic Support:</strong> Whether it's a difficult assignment, exam stress, or academic advice, our team of experts is available to provide guidance across various subjects and educational levels.</li>

        <li><strong>Emotional Well-being:</strong> We prioritize mental health and emotional well-being. Our counselors offer a compassionate ear, providing a safe space for students to express concerns and seek guidance on personal issues.</li>

        <li><strong>Career Guidance:</strong> Unsure about career choices or need advice on educational pursuits? Our advisors offer valuable insights to help students make informed decisions about their future pathways.</li>
    </ul>

    <h2>How to Reach Us</h2>

    Our Student Helpline is just a call or message away. Feel free to reach out to us via phone, email, or chat, and our dedicated team will be ready to assist you, providing immediate support and resources whenever you need it.
<br><br>
    <h2>Why Choose Us</h2>

    <ul>
        <li><strong>Prompt Assistance:</strong> Our team is available round-the-clock to ensure you get the help you need, precisely when you need it.</li>

        <li><strong>Expert Guidance:</strong> Count on our experienced professionals and counselors who are committed to providing the best support and advice.</li>

        <li><strong>Confidentiality:</strong> Your privacy and confidentiality are our utmost priority. Rest assured that all interactions are handled with complete discretion.</li>
    </ul>
'''
        },
        'studentHelp': {
            'content': '''
<h3>Student Helpline: Your Support System, Anytime, Anywhere</h3>

    At Manollasa, we understand the importance of accessible support for students navigating academic challenges and personal hurdles. Our Student Helpline operates round-the-clock, 24 hours a day, 7 days a week, to provide immediate assistance and guidance to students in need.
<br><br>
    <h2>What We Offer</h2>

    <ul>
        <li><strong>Academic Support:</strong> Whether it's a difficult assignment, exam stress, or academic advice, our team of experts is available to provide guidance across various subjects and educational levels.</li>

        <li><strong>Emotional Well-being:</strong> We prioritize mental health and emotional well-being. Our counselors offer a compassionate ear, providing a safe space for students to express concerns and seek guidance on personal issues.</li>

        <li><strong>Career Guidance:</strong> Unsure about career choices or need advice on educational pursuits? Our advisors offer valuable insights to help students make informed decisions about their future pathways.</li>
    </ul>
    <h2>How to Reach Us</h2>

Our Student Helpline is just a call or message away. Feel free to reach out to us via phone, email, or chat, and our dedicated team will be ready to assist you, providing immediate support and resources whenever you need it.
<br><br>
    <h2>Why Choose Us</h2>

    <ul>
        <li><strong>Prompt Assistance:</strong> Our team is available round-the-clock to ensure you get the help you need, precisely when you need it.</li>

        <li><strong>Expert Guidance:</strong> Count on our experienced professionals and counselors who are committed to providing the best support and advice.</li>

        <li><strong>Confidentiality:</strong> Your privacy and confidentiality are our utmost priority. Rest assured that all interactions are handled with complete discretion.</li>
    </ul>'''
        },
        'social': {
            'content': '''
        <h3 >Meet the Manollasa Social Service Team: Making an Impact, One Act of Kindness at a Time</h3>
        At Manollasa, we believe in giving back to society and fostering positive change. Our Social Service Team stands as a beacon of altruism, committed to making a meaningful difference in the lives of those in need.
<br><br>

        <h2>Our Mission</h2>

        The Manollasa Social Service Team is driven by the vision of creating a more inclusive and compassionate world. Our mission is to extend our hands and hearts to the underprivileged, marginalized communities, and the environment, fostering growth, empowerment, and sustainability.
<br><br>
        <h2>What We Do</h2>

        <ul>
            <li><strong>Community Outreach Programs:</strong> We organize and participate in various outreach programs aimed at addressing societal needs. From providing essential supplies to impoverished communities to organizing educational workshops, our team endeavors to uplift those in need.</li>

            <li><strong>Environmental Initiatives:</strong> Committed to environmental sustainability, we engage in eco-friendly initiatives. We promote awareness campaigns, tree plantation drives, and waste management programs to contribute to a greener planet.</li>

            <li><strong>Volunteer Opportunities:</strong> We encourage active involvement in our social endeavors. Volunteers play a pivotal role in our initiatives, amplifying our impact and spreading positivity in every endeavor.</li>

            <li><strong>Partnerships and Collaborations:</strong> Collaborating with like-minded organizations amplifies our reach and impact. Through strategic partnerships, we strive to create a more significant difference in the lives of those we serve.</li>
        </ul>

        <h2>How to Join Us</h2>

        Would you like to be part of our journey in creating a better world? Join our Social Service Team and contribute your time, skills, and passion to meaningful causes. Whether you're an individual, a corporate entity, or an organization, together, we can make a lasting impact.
<br><br>
        <h2>Get Involved</h2>

Reach out to us to learn more about our ongoing initiatives, partnership opportunities, or volunteer programs. Together, let's sow the seeds of positive change and build a brighter, more compassionate tomorrow.

The Manollasa Social Service Team: Where kindness meets action, and together, we create ripples of change across communities and the world.
    '''
        },
        'margadarshi': {
            'content': '''
<h3>Welcome to Manollasa Margadarshi: Empowering Futures</h3>

At Manollasa Margadarshi, we are dedicated to nurturing the aspirations of budding professionals and students, guiding them towards their envisioned career paths. Our commitment lies in providing unparalleled consultancy services, absolutely free of charge, to ambitious individuals seeking mentorship and advice.
<br><br>
<h4>Our Vision</h4>
We envision a world where every passionate student has access to invaluable guidance, paving the way for their success in their chosen fields. Manollasa Margadarshi is driven by the belief that mentorship and counsel are pivotal in shaping future leaders.
<br><br>
<h4>What We Offer</h4>

<strong>Free Consultancy for Students:</strong> Our team of seasoned professionals offers personalized guidance to students from various academic backgrounds. Whether you're navigating career choices, seeking advice on educational pursuits, or exploring professional pathways, our consultants are here to support you.
<br>
<strong>Career Development Assistance:</strong> We provide comprehensive support in mapping out your career journey. From resume building to interview preparation, we aim to equip you with the tools and insights essential for a successful transition into the professional world.
<br>
<strong>Industry Insights and Networking:</strong> Gain access to industry-specific knowledge and valuable connections. Through our network of experts, we offer insights into various fields, helping you gain a deeper understanding of your desired industry.
<br>
<strong>Continuous Learning Initiatives:</strong> Stay updated with the latest trends and developments in your field of interest. We offer workshops, seminars, and resources to ensure that you are always ahead in your pursuit of knowledge.
<br><br><h4>How to Engage With Us</h4>
Getting started with our free consultancy services is simple! Reach out to us through our contact form or schedule an appointment with one of our advisors. We are committed to assisting you in charting a path towards your dreams and ambitions.
<br>
At Manollasa Margadarshi, we believe in empowering dreams and shaping futures. Join us on this journey towards a brighter tomorrow!
'''
        }
    }

    def get(self, request, template_name):
        template = 'freeservice.html'
        data = self.data.get(template_name)

        if template:
            return render(request, template, context=data)
        else:
            return render(request, 'pagenotfound.html')
