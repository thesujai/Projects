<script>
    import {createEventDispatcher} from "svelte";
    import ProgressBar from "./ProgressBar.svelte";
    const totalSeconds = 40;
    let secondLeft = totalSeconds;
    let isRunning = false;
    const dispatch=createEventDispatcher();
    $: progress = ((totalSeconds - secondLeft) / totalSeconds) * 100;
    function startTimer() {
    isRunning = true;
    const timer = setInterval(() => {
      secondLeft -= 1;
      if (secondLeft == 0) {
        clearInterval(timer);
        isRunning = false;
        secondLeft = totalSeconds;
        dispatch('end');
      }
    }, 1000);
  }
</script>

<style>
    h2{
        margin: 0;
    }
    .start{
        background-color:rgb(140, 42, 42);
        width: 100%;
        margin: 10px 0;
    }
    .start[disabled]{
        background-color: rgb(194, 194, 194);
        cursor:wait;
    }
</style>
<div bp="grid">
    <h2 bp="offset-5@md 4@md 12@sm">
        Seconds Left:{secondLeft}
    </h2>
</div>
<ProgressBar {progress}/>
<div bp="grid">
<button  disabled={isRunning} bp="offset-5@md 4@md 12@sm"class="start" on:click={startTimer}>Start</button>
</div>