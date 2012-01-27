$(function() {

	$("#search").autocomplete({
		minLength : 2,
		delay : 500,
		source : "search.py",
		search : function(event, ui) {

			document.getElementById('search_loader').style.display = "block";
		},
		open : function(event, ui) {

			document.getElementById('search_loader').style.display = "none";
		},
		select : function(event, ui) {
			
			if (ui.item.Id != 0) {
				document.getElementById('loader').style.display = "block";
				$.get('fetchit.py', {
					song_id : ui.item.Id
				}, function(resp) {
					document.getElementById('search').value = "";

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
			else {
				document.getElementById('search').value = "";
			}

		},
		close : function(event, ui) {
			

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