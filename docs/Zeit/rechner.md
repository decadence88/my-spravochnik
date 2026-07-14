
<style> .md-content .md-typeset h1 { display: none !important; } </style>
<div class="calc-wrapper" style="max-width: 450px; margin: 10px auto; padding: 0 10px; font-family: Arial, sans-serif; text-align: center;">
    
    <div style="margin-bottom: 12px;">
        <input type="time" id="ankommen" value="07:58" style="padding: 12px 0; font-size: 26px; font-weight: bold; border-radius: 12px; border: none; text-align: center; width: 100%; max-width: 150px; background: var(--md-code-bg-color, #b0b3e7); color: var(--md-typeset-color, #b0b3e7); box-shadow: 0 2px 4px rgba(0,0,0,0.05); outline: none; -webkit-appearance: none; -moz-appearance: none; appearance: none; display: inline-block; justify-content: center;">
    </div>
    
    <div style="margin-bottom: 20px;">
        <input type="time" id="pause" value="00:02" style="padding: 12px 0; font-size: 26px; font-weight: bold; border-radius: 12px; border: none; text-align: center; width: 100%; max-width: 150px; background: var(--md-code-bg-color, #b0b3e7); color: var(--md-typeset-color, #b0b3e7); box-shadow: 0 2px 4px rgba(0,0,0,0.05); outline: none; -webkit-appearance: none; -moz-appearance: none; appearance: none; display: inline-block; justify-content: center;">
    </div>

    <style>
        input[type="time"]::-webkit-calendar-picker-indicator {
            background: none;
            display: none;
            -webkit-appearance: none;
        }
        input[type="time"]::-webkit-clear-button {
            -webkit-appearance: none;
            display: none;
        }
        input[type="time"]::-webkit-inner-spin-button {
            -webkit-appearance: none;
            display: none;
        }
    </style>

    <!-- Кнопка без неонового свечения -->
    <button onclick="berechnen()" style="width: 170px; height: 170px; border-radius: 50%; background: #545677; color: white; border: none; font-size: 26px; font-weight: bold; cursor: pointer; transition: background-color 0.2s; outline: none;" onmouseover="this.style.backgroundColor='#b0b3e7'" onmouseout="this.style.backgroundColor='#545677'">LOS</button>

    <!-- Результаты -->
<div id="result" style="display: none; margin-top: 20px; text-align: center; background: transparent; padding: 0; border: none; box-shadow: none;">
        
        <div style="margin-bottom: 20px; font-size: 22px; color: var(--md-typeset-color, #000);">
            <span style="opacity: 0.6; font-weight: normal; display: block; margin-bottom: 4px; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Feierabend Min</span>
            <span id="min" style="color: #b0b3e7; font-weight: 800; font-size: 36px; display: block;"></span>
        </div>
        
        <div style="font-size: 22px; color: var(--md-typeset-color, #000);">
            <span style="opacity: 0.6; font-weight: normal; display: block; margin-bottom: 4px; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Feierabend Max</span>
            <span id="max" style="color: #b0b3e7; font-weight: 800; font-size: 36px; display: block;"></span>
        </div>
        
    </div>
</div>

<script>
function addTime(time, add) {
    let [h1,m1] = time.split(":").map(Number);
    let [h2,m2] = add.split(":").map(Number);
    let totalMinutes = h1*60 + m1 + h2*60 + m2;
    let hours = Math.floor(totalMinutes / 60) % 24;
    let minutes = totalMinutes % 60;
    return String(hours).padStart(2,'0') + ":" + 
           String(minutes).padStart(2,'0');
}

function berechnen() {
    let ankommen = document.getElementById("ankommen").value;
    let pause = document.getElementById("pause").value;

    let muss_max = "08:59";
    let muss_min = "07:48";
    let pause_gesetz = "00:30";

    let feier_max;
    if (pause !== "00:00") {
        feier_max = addTime(addTime(ankommen, muss_max), pause);
    } else {
        feier_max = addTime(ankommen, muss_max);
    }

    let feier_min;
    if (pause < "00:30") {
        feier_min = addTime(addTime(ankommen, muss_min), pause_gesetz);
    } else {
        feier_min = addTime(addTime(ankommen, muss_min), pause);
    }

    document.getElementById("max").innerText = feier_max;
    document.getElementById("min").innerText = feier_min;

    document.getElementById("result").style.display = "block";
}
</script>