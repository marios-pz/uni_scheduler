var days = [
    'Κυριακή',
    'Δευτέρα',
    'Τρίτη',
    'Τετάρτη',
    'Πέμπτη',
    'Παρασκευή',
    'Σάββατο'
];

var months = [
    'Ιανουάριος',
    'Φεβρουάριος',
    'Μάρτιος',
    'Απρίλιος',
    'Μάιος',
    'Ιούνιος',
    'Ιούλιος',
    'Αύγουστος',
    'Σεπτέμβριος',
    'Οκτώβριος',
    'Νοέμβριος',
    'Δεκέμβριος'
];

function startTime() {
  const today = new Date();
  let h = today.getHours();
  let m = today.getMinutes();
  let s = today.getSeconds();
  let day = days[ today.getDay() ];
  let month = months[ today.getMonth() ];
  let year = today.getFullYear()
  m = checkTime(m);
  s = checkTime(s);

  let uses = 0;

  let output = day + " " + h +':'+ m +':' + s + " " + month + " " + year;

  // automate data refreshing
  if(m == 0 && s == 0)
  {
      document.location.reload(true)
  }

  try{
      if(m > 0)
      {
          document.getElementById('clock').innerHTML =  output + '<br />' + "έχεις αργήσει " + m + " λεπτά!";
      }
      else
      {
          document.getElementById('clock').innerHTML =  output;
      }

      setTimeout(startTime, 1000);

  } catch (e) {
      console.log("Its weekend")
  }
}



function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}

