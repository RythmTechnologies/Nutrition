
document.addEventListener('DOMContentLoaded', function() {
    const datepicker = flatpickr('.flatpickr-date', {
      altInput: true,
      altFormat: "F j, Y",
      dateFormat: "Y-m-d",
      minDate: "today",
      maxDate: new Date().fp_incr(365),
      locale: 'tr',
      disable: [
        function(date) {
          return date.getDay() === 0;
        }
      ],
      onChange: function(selectedDates, dateStr, instance) {
        const date = selectedDates[0];
        if (date && date.getDay() === 6) { 
          timepicker.set('minTime', '10:00');
          timepicker.set('maxTime', '13:30');
        } else {
          timepicker.set('minTime', '10:00');
          timepicker.set('maxTime', '18:30');
        }
      }
    });
    const timepicker = flatpickr('.flatpickr-time', {
      enableTime: true,
      noCalendar: true,
      dateFormat: "H:i",
      minTime: "9:00",
      maxTime: "18:30",
      time_24hr: true,
      minuteIncrement: 15,
    });
  });