import { mobileOperation } from "./mobile/index-mobile.js";
import { carouselOperation } from "./exports/carrossel.js";
import { formsValidation } from "./exports/forms-validation.js";
import { loadProfile } from "./exports/load-porfile.js";
import { toggleMenu } from "./exports/load-porfile.js";
import { bookedAppointments } from "./exports/reserved-schedules.js";
import { getName } from "./exports/profile-dropdown.js";

mobileOperation();
carouselOperation();
formsValidation();
// loadProfile();
toggleMenu();
bookedAppointments();
getName();