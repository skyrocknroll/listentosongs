//Facebook Login Button

//(function(d, s, id) {
//  var js, fjs = d.getElementsByTagName(s)[0];
//  if (d.getElementById(id)) return;
//  js = d.createElement(s); js.id = id;
//  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=259978174072633";
//  fjs.parentNode.insertBefore(js, fjs);
//}(document, 'script', 'facebook-jssdk'));



// Facebook Like and Recommend Button
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_GB/all.js#xfbml=1&appId=259978174072633";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


function statusAnimate(){
	$("#InfoId").fadeTo(1000,0,function(){
		$("#InfoId").fadeTo(1000,1);
	}
	);
}
var setIntervalId = 0;
var language = "Tamil";
var songSelected = false;
$(function() {

	$("#search").autocomplete({
		minLength : 2,
		delay : 500,
		
		search : function(event, ui) {
			language = "Tamil";
			for ( var i =0 ; i < document.getElementsByName("langName").length ; i ++){
				if(document.getElementsByName("langName")[i].checked == true){
					language = document.getElementsByName("langName")[i].value;
					//alert(language);
					document.getElementById("language").value = language;
				}
			};
			$(function(){
				$("#search").autocomplete({
					source : "search.py?lang="+language
				});
			});	
			document.getElementById('search_loader').style.display = "block";
		},
		
		open : function(event, ui) {

			document.getElementById('search_loader').style.display = "none";
		},
		select : function(event, ui) {
			songSelected = true;
			//alert(songSelected );
			if (ui.item.Id != 0) {
				
				//document.getElementById('loader').style.display = "block";
				$("#InfoId").css('visibility','visible');
				 setIntervalId = setInterval("statusAnimate()", 2000);
					
				$.get('fetchit.py', {
					song_id : ui.item.Id,
					lang:document.getElementById("language").value
				}, function(resp) {
					clearInterval(setIntervalId);
					$("#InfoId").css('visibility','hidden');

//					document.getElementsByTagName('audio')[0].src = resp.src;
//					document.getElementsByTagName('audio')[0].play();
//					playlistItem = '{title:"'+resp.title+'" , mp3:"'+ resp.src +'"}';
//					alert(playlistItem);
					MyPlayList.add({title:resp.title , mp3:resp.src});
					if(MyPlayList.playlist.length == 1){
						MyPlayList.play();
					}
					document.getElementById('loader').style.display = "none";

				});
			}
			

		},
		close : function(event, ui) {
			if(songSelected){
				document.getElementById('search').value = "";
			}
			songSelected = false;

		}
	});
});




// Jplayer

$(document).ready(function() {

	MyPlayList = new jPlayerPlaylist({
		jPlayer : "#jquery_jplayer_2",
		cssSelectorAncestor : "#jp_container_2"
	}, [

	], {
		playlistOptions: {
			enableRemoveControls: true,
			autoPlay:true
			},
		swfPath : "js",
		supplied : "mp3",
		wmode : "window"
	});
});

$("#jquery_jplayer_2").jPlayer("size", {width: "700px"}) ; 

$(document).ready(function() {
	 language = "Tamil";
	for ( var i =0 ; i < document.getElementsByName("langName").length ; i ++){
		if(document.getElementsByName("langName")[i].checked == true){
			language = document.getElementsByName("langName")[i].value;
		}
		
	}
	

	//document.getElementById("playlist-options_id").style.display = "none";
});


function playRandomSongs(){
	
	// Remove all the previous songs in the playlist
	MyPlayList.remove();
	language = "Tamil";
	for ( var i =0 ; i < document.getElementsByName("langName").length ; i ++){
		if(document.getElementsByName("langName")[i].checked == true){
			language = document.getElementsByName("langName")[i].value;
			//alert(language);
			document.getElementById("language").value = language;
		}
	};
	
	$.get('localRandomPlay.py', {
		lang:document.getElementById("language").value
	}, function(resp) {
		randPlaylist = jQuery.parseJSON(resp);
		for (var k= 0 ; k < randPlaylist.length ; k++){
			MyPlayList.add({title:randPlaylist[k].title , mp3:randPlaylist[k].src});
		}
		MyPlayList.play(0);
	});
	
	return false;
}

function clearPlaylist(){
	MyPlayList.remove();
	return false;
}