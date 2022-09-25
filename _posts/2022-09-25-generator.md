---
toc: true
layout: post
categories: [markdown]
title: Java NBA Team Generator
---
## Click the button below and it will generate a random nba team

<button name="button" onclick="get_random()">Click for Random NBA team</button>
<p id="Random NBA Team"></p>
<script>
function get_random () {
    const list = ["Lakers", "Clippers", "Warriors", "Kings", "Knicks", "Nets", "Bucks", "Cavs", "Bulls", "Hawks", "Celtics", "Pistons", "Suns", "Heat", "Jazz" ]
    document.getElementById("Random NBA Team").innerHTML = list[Math.floor((Math.random()*list.length))];
  }
</script>