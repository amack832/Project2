<my-timer>

  <p>Minimum javascript library requirements have been met on this page for {time} seconds.</p>
  
  <style>
	:scope {
		animation: fancy 1s linear infinite;
		color: red;
		font-size: 15px;
	}
	
	

	@keyframes fancy {
		75% {color: blue};
	}
  </style>
  
  <script>
	this.time = 0;
	
	tick (){
		this.update({time: ++ this.time});
	}
	
	const timer = setInterval(this.tick,1000);
	// http://css-tricks.com/snippets/css/keyframe-animation-syntax/
	// ensure that interval is cleared when component not in use
	this.on('unmount',() => clearInterval(timer));
  </script>
	
</my-timer>