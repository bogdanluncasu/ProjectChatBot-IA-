			var player;		  
			var ws;
			var loaded=false;
			var loadedplayer=false;
			var game = new Phaser.Game(900, 500, Phaser.AUTO, 'cchat', { preload: preload, create: create, update: update });
				
					function preload() {
						game.load.spritesheet('talk', 'assets/talk_sprite.png',107,130);
						game.load.image('bg', 'assets/bg.jpg');
					}

					function create() {
						game.physics.startSystem(Phaser.Physics.ARCADE);
						bg = game.add.image(0, 0, 'bg');
						player = game.add.sprite(0, 0, 'talk');
						loadedplayer=true;
						player.width=145;
						player.height=150;
						bg.width=900;
						bg.height=500;
						


						player.animations.add('left', [0, 1, 2, 3], 10, true);
						player.animations.add('stop', [0], 10, true);
						player.animations.add('right', [5, 6, 7, 8], 10, true);
						
						


					}



					function update() {
						
					}

					  function startDictation() {
					 
						if (window.hasOwnProperty('webkitSpeechRecognition')) {
					 
						  var recognition = new webkitSpeechRecognition();
					 
						  recognition.continuous = false;
						  recognition.interimResults = false;
					 
						  recognition.lang = "en-US";
						  recognition.start();
					 
						  recognition.onresult = function(e) {
							document.getElementById('transcript').value
													 = e.results[0][0].transcript;
							recognition.stop();
							document.getElementById('labnol').submit();
						  };
					 
						  recognition.onerror = function(e) {
							recognition.stop();
						  }
					 
						}
					  }
			function gobottom(){
				var elem = document.getElementById('chat');
				elem.scrollTop = elem.scrollHeight;
			}
					  
			$(document).ready(function(){
				
				if ("WebSocket" in window)
				{
					ws = new WebSocket("ws://chatbot-server.herokuapp.com/");
					loaded=true;
					window.setInterval(function() {
					   ws.send("");
					}, 1000);
					ws.onmessage = function (evt) {
							index=0;
							interval=window.setInterval(function() {
								if(loadedplayer){
									player.animations.play('left');
								}
							   index+=1;
							   if(index>~~(evt.data.length/14)){
									clearInterval(interval);
									player.animations.play('stop');
							   }
							}, 1000);
							

							
						
						var received_msg = evt.data;
						responsiveVoice.speak(received_msg.slice(5,received_msg.length));
						console.log("Received: " + received_msg);
						$("#chat").append("<div class='chatbox__messages__robot-message'><p class='message'>"+received_msg+"</p></div>")
						gobottom();
					};
							
					ws.onclose = function(){
						
						$("#chat").append("<div class='chatbox__messages__robot-message'><p class='message'>Bot> Hey. I need to go. Bye.</p></div>")
						gobottom();
					};
				}else{
					alert("WebSocket NOT supported by your Browser!");
				}
						
		

			});
			
			$(document).keypress(function(e) {
				
				if(e.which == 13){
					msg=$('#msg').val();
					console.log(msg);
					if($("#chat").get(0).childElementCount!=0 && loaded){
						$("#chat").append("<div class='chatbox__messages__user-message'><p class='message'>"+msg+"</p></div>")
						ws.send(msg);
						$("#msg").val('');
					}
				}
			});