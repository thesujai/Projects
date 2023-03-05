<script>
	import HowTo from "./HowTo.svelte";
	import Timer from "./Timer.svelte";
	let audio;
	function playAudio() {
		audio.play()
	}
</script>
<style>
	h1{
		text-align: center;
	}
	h3{
		text-align: center;
	}
</style>

<h1>Handwashing App</h1>


<Timer on:end={playAudio}/>
<HowTo/>
<h3>
<a href="https://cdn.who.int/media/docs/default-source/patient-safety/how-to-handwash-poster.pdf?sfvrsn=7004a09d_8">Image Source</a>
<a href="https://freesound.org/people/metrostock99/sounds/345086/">Sound Source</a>
</h3>

<audio bind:this={audio}>
	<source src='HandwashSound.wav' />
</audio>