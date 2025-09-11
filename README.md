# **Workshop Booking**

> This website is for coordinators to book a workshop(s), they can book a workshop based on instructors posts or can propose a workshop date based on their convenience.

***

### Features

* Statistics
  1. Instructors Only
     * Monthly Workshop Count
     * Instructor/Coordinator Profile stats
     * Upcoming Workshops
     * View/Post comments on Coordinator's Profile
  2. Open to All
     * Workshops taken over Map of India
     * Pie chart based on Total Workshops taken to Type of Workshops.

* Workshop Related Features
  > Instructors can Accept, Reject or Delete workshops based on their preference, also they can postpone a workshop based on coordinators request.

__NOTE__: Check docs/Getting_Started.md for more info.

***

## What design principles guided your improvements?

My improvements were guided by three core design principles:

* **Mobile-First Responsive Design:** I started by designing for mobile devices and then progressively enhanced the layout for larger screens. I used **CSS Grid** and **Flexbox** to create flexible layouts that automatically adapt to content and implemented specific **breakpoints** at `1200px`, `992px`, `768px`, `576px`, and `420px` to ensure fine-grained control over the layout at various screen sizes.
* **Visual Hierarchy & Accessibility:** I maintained a clear information structure with proper heading tags. I used color contrast ratios that meet accessibility standards to ensure content is readable for everyone. Interactive elements, like buttons and links, were given a minimum touch target of **44px** to make them easy to tap on touch devices.
* **Progressive Enhancement:** The application's core functionality is built to work without JavaScript. I then added enhancements like hover effects, animations, and dynamic interactions using JavaScript to improve the user experience for modern browsers. This approach ensures graceful degradation if any of these features are not supported.

***

## How did you ensure responsiveness across devices?

To ensure responsiveness, I followed a multi-faceted strategy:

1.  **Flexible Layout System:** The entire layout is built on a flexible foundation. Containers and media elements like images and videos have a `max-width: 100%`, allowing them to scale automatically. I used `clamp()` for flexible typography, which makes font sizes scale proportionally with the viewport.
2.  **Breakpoint-Specific Adjustments:** I implemented specific layouts for different device categories.
    * **Desktop (1200px+)**: A side-by-side layout with full features.
    * **Tablet (768px-1200px)**: A stacked layout with reduced padding.
    * **Mobile (≤768px)**: A single-column layout with compact spacing.
3.  **Touch-Friendly Interface:** I increased button padding to make them easier to press with a finger. I also implemented **horizontal scrolling** for wide tables, which prevents them from overflowing and breaking the page layout on small screens.

***

## What trade-offs did you make between the design and performance?

I made deliberate trade-offs to prioritize performance and reliability:

* **CSS vs. JavaScript:** I chose to use **CSS-only responsive design** for all layout changes. This provided less dynamic control than JavaScript, but it resulted in faster rendering and ensures the layout works even if a user has JavaScript disabled.
* **Image Optimization:** I used **CSS background images** with `background-size: cover`. This is a simpler approach than using complex image loading scripts. The trade-off is less control over loading states, but the benefit is a faster, more reliable implementation that automatically scales images to fit their containers.
* **Animation Performance:** I relied on **CSS transitions** for animations instead of JavaScript. While this limits the complexity of the animations, it allows them to be hardware-accelerated, providing a smoother, more performant user experience.

***

## What was the most challenging part of the task and how did you approach it?

The most challenging part of the task was implementing the **navbar hover expansion feature**.

The problem was to create a smooth and accessible hover interaction that:
* Expands the navbar to double its height.
* Changes the background color.
* Reveals a new description panel below the existing navbar items.
* Works seamlessly across different screen sizes.
* Maintains accessibility for keyboard users.

My solution involved a hybrid approach using both CSS and JavaScript. I used a **CSS-only expansion** with `max-height` and `opacity` transitions for the animation itself, which provides better performance. A **Flexbox layout** ensured proper stacking and alignment of the navbar items and the new description panel. I used **JavaScript event handling** to manage the hover and focus states, ensuring the feature is accessible to keyboard users and touch devices.

The key learning was the importance of balancing visual impact with usability. I had to carefully consider the timing and spacing of the animations, and create fallback states for users who cannot hover (e.g., on touch devices). The result is a polished, responsive interface that works flawlessly across all device types while staying true to the original design intent.

`LOGIN PAGE`
### Before
![Image Description](/workshop_app/static/workshop_app/img/oldLoginPage.png)
### After
![Image Description](/workshop_app/static/workshop_app/img/newLoginPage.png)

`LOGOUT PAGE`
### Before
![Image Description](/workshop_app/static/workshop_app/img/oldLogoutPage.png)
### After
![Image Description](/workshop_app/static/workshop_app/img/newLogoutPage.png)

`SIGN IN PAGE`
### Before
![Image Description](/workshop_app/static/workshop_app/img/oldSignInpage.png)
### After
![Image Description](/workshop_app/static/workshop_app/imG/newSignInPage.png)

`PROPOSE WORKSHOP`
### Before
![Image Description](/workshop_app/static/workshop_app/img/oldProposeWorkshop.png)
### After
![Image Description](/workshop_app/static/workshop_app/img/newProposeWorkshop.png)

`WORKSHOP TYPES`
### Before
![Image Description](/workshop_app/static/workshop_app/img/oldWorkshopTypesPage.png)
### After
![Image Description](/workshop_app/static/workshop_app/img/newWokshopTypesPage.png)

`ADD NEW WORKSHOP PAGE`
### Before
![Image Description](/workshop_app/static/workshop_app/img/oldEditWorkshopPage.png)
### After (added back to workshop types tab button also)
![Image Description](/workshop_app/static/workshop_app/img/newAddWorkshopPage.png)

`PROFILE VIEW PAGE`
### Before
![Image Description](/workshop_app/static/workshop_app/img/oldProfileView.png)
### After 
![Image Description](/workshop_app/static/workshop_app/img/newProfileviewPAge.png)

`STATUS AND HOME PAGE`
### Before
![Image Description](/workshop_app/static/workshop_app/img/oldHomeAndStatusPAgeInstructor.png)
### After 
![Image Description](/workshop_app/static/workshop_app/img/newStatusAndHomePAge.png)

`WORKSHOP STATISTICS PAGE`
### Before
![Image Description](/workshop_app/static/workshop_app/img/oldWorkshopStatistics.png)
### After 
![Image Description](/workshop_app/static/workshop_app/img/newWorkshopStatisticsPage.png)