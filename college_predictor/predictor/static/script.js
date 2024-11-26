/*sliding images*/
document.addEventListener('DOMContentLoaded', function () {
    let currentIndex = 0;
    const items = document.querySelectorAll('.carousel-item');
    const totalItems = items.length;


    function showCurrentItem() {
        items.forEach((item, index) => {
            item.classList.remove('active', 'next', 'prev');
            if (index === currentIndex) {
                item.classList.add('active');
            } else if (index === (currentIndex + 1) % totalItems) {
                item.classList.add('next');
            } else if (index === (currentIndex - 1 + totalItems) % totalItems) {
                item.classList.add('prev');
            }
        });
    }

    function changeImage() {
        currentIndex = (currentIndex + 1) % totalItems; 
        showCurrentItem();
    }

    showCurrentItem();

    setInterval(changeImage, 4000);
});


//servies//
function toggleDetails(serviceId) {
    const detailsElement = document.getElementById(serviceId);
    const currentDisplay = detailsElement.style.display;

    if (currentDisplay === 'none' || currentDisplay === '') {
        detailsElement.style.display = 'block';
    } else {
        detailsElement.style.display = 'none';
    }
}


/*testimonials*/
let currentIndex = 0;
const testimonials = document.querySelectorAll('.testimonial');
const totalTestimonials = testimonials.length;

function showTestimonials() {
    testimonials.forEach((testimonial, index) => {
        testimonial.style.transform = `translateX(${(index - currentIndex) * 100}%)`;
    });
}


function changeTestimonials() {
    currentIndex++;

    if (currentIndex >= totalTestimonials) {
        currentIndex = 0;

        testimonials.forEach(testimonial => {
            testimonial.style.transition = 'none'; 
            testimonial.style.transform = `translateX(100%)`; 
        });

        setTimeout(() => {
            testimonials.forEach(testimonial => {
                testimonial.style.transition = 'transform 1s ease-in-out'; 
            });

            currentIndex = 0;
            showTestimonials();
        }, 50); 
    } else {
        showTestimonials();
    }
}

showTestimonials();

const testimonialInterval = setInterval(changeTestimonials, 2000);

const serviceLinks = document.querySelectorAll('.service-link');
const serviceDetails = document.getElementById('service-details');
const serviceDescription = document.getElementById('service-description');
const serviceImage = document.getElementById('service-image');
const closeDetailsButton = document.getElementById('close-details');

const serviceInfo = {
    personalized: {
        description: "Personalized College Predictions help you understand which colleges might be the best fit for you based on your profile.",
        image: "https://via.placeholder.com/150?text=Personalized+Predictions"
    },
    evaluation: {
        description: "Profile Evaluation involves a thorough analysis of your academic and extracurricular achievements to provide tailored advice.",
        image: "https://via.placeholder.com/150?text=Profile+Evaluation"
    },
    guidance: {
        description: "Admission Guidance offers insights into the application process, including tips on writing essays and preparing for interviews.",
        image: "https://via.placeholder.com/150?text=Admission+Guidance"
    },
    counseling: {
        description: "Career Counseling assists you in exploring various career paths and making informed decisions about your future.",
        image: "https://via.placeholder.com/150?text=Career+Counseling"
    }
};

serviceLinks.forEach(link => {
    link.addEventListener('click', function (event) {
        event.preventDefault();
        const serviceKey = this.getAttribute('data-service');
        serviceDescription.textContent = serviceInfo[serviceKey].description;
        serviceImage.src = serviceInfo[serviceKey].image;
        serviceDetails.style.display = 'block';
    });
});

closeDetailsButton.addEventListener('click', function () {
    serviceDetails.style.display = 'none';
});

