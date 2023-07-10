---
layout: '../../layouts/main.astro'
title: 'Acknowledgement'
date: 2023-07-09
---

<!-- ----------------------- load all required sources ---------------------- -->
<script src="https://unpkg.com/@dotlottie/player-component@1.0.0/dist/dotlottie-player.js"></script>


<!--  ======================================================================== -->
<!--  ============================= start article ============================ -->
<!--  ======================================================================== -->
<article class="prose">

# Acknowledgement

<!-- <div class="text-base"> -->
All praise and thanks to the 

<!-- -------------------------- bismillah animation ------------------------- -->
<!-- grid gives each item the same space - not desired here -->
<!-- <div class="grid grid-cols-2 gap-4 "> -->
<!-- <div class="grid grid-cols-2 gap-1 place-items-center"> -->

<!-- flex consideres each element for itself - takes only as much space as required by default -->
<div class="flex justify-center items-center my-10">

  <div class="w-1/3 flex justify-center 
              items-center
              text-3xl" >
  <strong>ONE</strong>
  </div>

  <div class="w-2/3 flex justify-center items-center" id="bismillah_Anim">
  <!-- the bismillah file is obtained through:https://lottiefiles.com/4098-bismillah-in-the-name-of-allah?lang=de 
and https://lottiefiles.com/xylam -->

  <dotlottie-player
    id="bismillah"
    class="bismillah_Anim"
    autoplay
    loop
    src="0_Lotti/bismillah.lottie"
    mode="bounce"
    style="width: 100%"></dotlottie-player>
  </div>
    <!-- src="../../src/assets/0_Lotti/bismillah.lottie" -->

</div>

, Who does neither need my praise nor my thanks. To the 

<!-- --------------------------- mosque animation --------------------------- -->
<div class="flex justify-center items-center my-10">
  <div class="w-2/3 flex justify-center
              items-center" id="mosque_Anim">
  <!-- the mosque file is obtained through:https://lottiefiles.com/102940-faisal-mosque?lang=de and https://lottiefiles.com/ranaadeelfarrukh -->
  <dotlottie-player
    id="bismillah"
    class="mosque_Anim"
    autoplay
    speed="2"
    loop
    mode="bounce"
    src="0_Lotti/mosque.lottie"
    style="width: 100%"></dotlottie-player>
  </div>

  <div class="w-1/3 flex justify-center 
              items-center
              text-3xl">
  <strong>ONE</strong>
  </div>

</div>


, Who is independent of everything and everyone, but on Whom everything and everyone depends.

<!-- </div> -->

</article >

