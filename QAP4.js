alert("hello world");


const motelCustomer = {
    identification: "J800124066",
    first: "Jill",
    last: "Java",
    birthYear: "1980",
    birthMonth: "January",
    birthDay: "24",
    gender: "Female",
    roomPreferences:["King Bed", "Double Bed", "Queen Bed", "Balcony", "Ocean View", "Garden View", "Pet Friendly"],
    paymentMethod: "Credit Card",

    vehicle: {
        year: "2022",
        make: "Ford",
        model: "F150",
        licPlate: "CGM340",
    },

    address:{
        street: "123 Java Lane",
        city: "Corner Brook",
        province: "NL",
        postalCode: "J1J4V4",
        country: "Canada",
    },

    phoneNumber: "709-123-4567",

    checkIn:{
        date:new Date(2023, 6, 15, 14, 0),   
        
    },

    checkOut:{
        date:new Date(2023, 6, 17, 11, 0),
    },

    calculateAge: function(){
        const today = new Date();
        return today.getFullYear() - this.birthYear;
    },

    calculateDurationOfStay: function () {
        const checkIn = this.checkIn.date;
        const checkOut = this.checkOut.date;
        const oneDay = 1000 * 60 * 60 * 24; 
        return Math.round((checkOut - checkIn) / oneDay);
    },
    
};

console.log(motelCustomer)

let html;

html = `<h2> Motel Customer Information</h2>
<p><strong>Name:</strong> ${motelCustomer.first} ${motelCustomer.last}</p>
<p><strong>Age:</strong> ${motelCustomer.calculateAge()}</p>
<p><strong>Gender:</strong> ${motelCustomer.gender}</p>
<p><strong>Room Preferences:</strong> ${motelCustomer.roomPreferences.join(", ")}</p>
<p><strong>Payment Method:</strong> ${motelCustomer.paymentMethod}</p>
<p><strong>Mailing Address:</strong><br>${motelCustomer.address.street}<br>${motelCustomer.address.city}, ${motelCustomer.address.province} ${motelCustomer.address.postalCode}<br>${motelCustomer.address.country}</p>
<p><strong>Vehicle:</strong><br>${motelCustomer.vehicle.year} ${motelCustomer.vehicle.make} ${motelCustomer.vehicle.model} ${motelCustomer.vehicle.licPlate}</p>
<p><strong>Phone Number:</strong> ${motelCustomer.phoneNumber}</p>
<p><strong>Check-In Date:</strong> ${motelCustomer.checkIn.date.toLocaleString()}</p>
<p><strong>Check-Out Date:</strong> ${motelCustomer.checkOut.date.toLocaleString()}</p>
<p><strong>Duration of Stay:</strong> ${motelCustomer.calculateDurationOfStay()} days</p>
`;

console.log(html)

document.body.innerHTML = html;