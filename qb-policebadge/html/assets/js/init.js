const open = (data) => {
  $('#name').css('color', '#282828');

  $('#name').text(data.name);
  $('#rankName').text(data.rankName);
  $('#callsign').text(data.callsign);
  let job = data.job;
  let rank = data.rank
  let cid = data.cid
  if (cid == "OMT96943") {
    $('#id-card').css('background', 'url(assets/images/spacecommand.png)');
  } else if (job == "highway") {
    $('#id-card').css('background', 'url(assets/images/sahp.png)');
  } else if (job == "fib") {
    $('#id-card').css('background', 'url(assets/images/fib.png)');
  } else if (job == "ambulance") {
    $('#id-card').css('background', 'url(assets/images/safr.png)');
  } else if (job == "judge") {
    $('#id-card').css('background', 'url(assets/images/doj.png)');
  } else {
    if (job == "police") {
    if (rank > 0 && rank <= 9) {
      $('#id-card').css('background', 'url(assets/images/lspd-silver-badge.png)');
    } else if (rank >= 10 && rank <= 13) {
      $('#id-card').css('background', 'url(assets/images/lspd-silver-gold-badge.png)');
    } else if (rank >= 15) {
      $('#id-card').css('background', 'url(assets/images/lspd-gold-badge.png)');
    } else {
      $('#id-card').css('background', 'url(assets/images/lspd-cadet.png)');
    }}
  }

    $('#id-card').show();
  }

const close = () => {
  $('#name').text('');
  $('#rankName').text('');
  $('#height').text('');
  $('#callsign').text('');
  $('#sex').text('');
  $('#id-card').hide();
  $('#licenses').html('');
}

$(document).ready(function(){
    window.addEventListener('message', function(event) {
        switch(event.data.action) {
            case "open":
                open(event.data);
                break;
            case "close":
                close();
                break;
        }
    })
});
