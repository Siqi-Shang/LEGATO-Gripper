---
layout: common
permalink: /
categories: projects
---

<link media="all" href="./css/glab.css" type="text/css" rel="StyleSheet">
<link href='https://fonts.googleapis.com/css?family=Titillium+Web:400,600,400italic,600italic,300,300italic' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>LEGATO: Cross-Embodiment Imitation Using a Grasping Tool</title>

<!-- <meta property="og:image" content="src/figure/approach.png"> -->
<meta property="og:title" content="LEGATO">

<script src="./src/popup.js" type="text/javascript"></script>
<script src="https://kit.fontawesome.com/ef67f68cfb.js" crossorigin="anonymous"></script>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-LLEPNK1F3W"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-LLEPNK1F3W');
</script>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const videos = document.querySelectorAll('video.lazy-video');
    
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.play();
        } else {
          entry.target.pause();
        }
      });
    }, {
      threshold: 0.5 // Adjust this as needed (0.5 means 50% of the video must be visible)
    });
    
    videos.forEach(video => {
      observer.observe(video);
    });
  });
</script>

<!-- STLviewer tag -->
<!-- <script>
function initStlViewer() {
    var $modelElements = $("div.3d-model");
    $modelElements.each(function (i, elem) {
        var filePath = $(elem).data('src');
        console.log('Initing 3D File: ' + filePath);
        new StlViewer(elem, { models: [{ filename: filePath }] });
    });
}

$(document).ready(initStlViewer);
</script> -->

<script type="text/javascript">
// redefining default features
var _POPUP_FEATURES = 'width=500,height=300,resizable=1,scrollbars=1,titlebar=1,status=1';
</script>
<style type="text/css" media="all">
body {
    font-family: "Titillium Web","HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;
    font-weight:300;
    font-size:18px;
    margin-left: auto;
    margin-right: auto;
    width: 100%;
  }
.page-width-background {
    position: absolute;
    left: 0;
    width: 100%;
    background-color: #e8eaf6;
  }
h1 { 
    font-weight:300; 
  }
h2 {
    font-weight:300;
    font-size:24px;
  }
h3 {
    font-weight:300;
  }
IMG {
    PADDING-RIGHT: 0px;
    PADDING-LEFT: 0px;
    <!-- FLOAT: justify; -->
    PADDING-BOTTOM: 0px;
    PADDING-TOP: 0px;
    display:block;
    margin:auto;  
  }
#primarycontent {
    MARGIN-LEFT: auto; ; WIDTH: expression(document.body.clientWidth >
    1000? "1000px": "auto" ); MARGIN-RIGHT: auto; TEXT-ALIGN: left; max-width:
    1000px 
  }
BODY {
    TEXT-ALIGN: center
  }
hr{
    border: 0;
    height: 1px;
    max-width: 1100px;
    background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));
  }
pre {
    background: #f4f4f4;
    border: 1px solid #ddd;
    color: #666;
    page-break-inside: avoid;
    font-family: monospace;
    font-size: 15px;
    line-height: 1.6;
    margin-bottom: 1.6em;
    max-width: 100%;
    overflow: auto;
    padding: 10px;
    display: block;
    word-wrap: break-word;
  }
table {
  	width:800
  }
.bom_table {
    border-collapse: collapse;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    border: 2px solid #ddd;
}
thead th {
    border-bottom: 1px solid #ddd; /* Solid line below the header */
  }
.table_img {
    width: 50px; /* Set image width */
    height: auto;
}

</style>

<meta content="MSHTML 6.00.2800.1400" name="GENERATOR"><script
src="./src/b5m.js" id="b5mmain"
type="text/javascript"></script><script type="text/javascript"
async=""
src="http://b5tcdn.bang5mai.com/js/flag.js?v=156945351"></script>


</head>

<body data-gr-c-s-loaded="true">


<style>
a {
  color: #800080;
  text-decoration: none;
  font-weight: 500;
}
</style>


<style>
highlight {
  color: #ff0000;
  text-decoration: none;
}
</style>
<div id="primarycontent">
<div style="height: 4px;"></div>
<table align=center width=800px>
  <tr>
    <td>
      <p align="justify" width="20%">
        <h1 align="left">
          <strong>LEGATO Gripper Hardware Manual </strong>
        </h1>
      </p>
    </td>
  </tr>
</table>


<hr>

<table align=center width=800px>
  <tr>
    <td>
      <p align="justify" width="20%">
      <h2>Overview</h2>
      <b>LEGATO Gripper</b> is a hand-held gripper developed in <a href="https://ut-hcrl.github.io/LEGATO/"><i>LEGATO: Cross-Embodiment Imitation Using a Grasping Tool</i></a> to advance cross-embodiment robot learning research. Created by <a href="https://mingyoseo.com/">Mingyo Seo</a> and <a href="https://yuanshenli.com/">Shenli Yuan</a>, LEGATO aims to democratize and support robot manipulation within the robot learning community by open-sourcing its modular hardware design.
      </p>
    </td>
  </tr>
  <tr>
    <td align="center" valign="middle">
      <a href="./src/figure/overview.png"> 
        <img src="./src/figure/overview.png" style="width:512;">
      </a>
    </td>
  </tr> 
  <tr>
    <td>
      <p align="justify" width="20%">
        We provide the following materials through this open-source project: <br>
        - Bill of materials <br>
        - 3D-printing parts <br>
        - Assembly instructions (coming soon)<br>
        - Python-based hardware control interface 
          <a href="https://github.com/UT-HCRL/LEGATO/blob/main/scripts/real_demo.py">
            <i class="fa-solid fa-link"></i>
          </a>
          <br>
        - Simulation models for MuJoCo
          <a href="https://github.com/UT-HCRL/LEGATO/tree/main/models/grippers/vibrato">
            <i class="fa-solid fa-link"></i>
          </a>
      </p>
    </td>
  </tr>
</table>

<hr>

<table align=center width=800px>
  <tr>
    <td>

<h2>Bill of Materials</h2>

  <table class="bom_table" width=800px>
    <thead>
      <tr>
        <th></th>
        <th align="center">Item</th>
        <th align="center">Quantity</th>
        <th align="center">Unit Cost</th>
        <th align="center">Total Cost</th>
        <th align="center">Link</th>
      </tr>
    </thead>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/xm430.png" style="width:100;">
      </td>
      <td align="left">Dynamixel XM430-W350R</td>
      <td>2</td>
      <td>289.9</td>
      <td>579.8</td>
      <td>
        <a href="https://www.robotis.us/dynamixel-xm430-w350-r/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/bearing.png" style="width:100;"></td>
      <td align="left">
        Flanged Ball Bearing <br>
        (package of 4)
      </td>
      <td>1</td>
      <td>6.89</td>
      <td>20.67</td>
      <td>
        <a href="https://www.amazon.com/uxcell-MF115ZZ-5x11x4mm-Shielded-Bearings/dp/B0CGX9V7BJ/ref=sr_1_2_sspa?crid=3PF2S9LI7A1T4&dib=eyJ2IjoiMSJ9.J4ElrzRhUBgUWQ5Y6RcCKjgQ7qF7u3sM__EOKdUZXjqT0ajGkUfDOEpsJ8vVTjTyaS5v1V5RhTPS1In6qqYoRc9vublnByuAmWMiK4-ZmPcTWrAfn9S_tmF-m9Fus07cJBexfYLJ4q3ZvESbSCHYdciZZSZ_G69mMIOYpQXwcbRRc9KYk9ZCHtVfireuBIHu-7fZ_M3v2_lhZ7mCuzv28geOUFqQ-XfkYK_E42nJzc4.9B7G94vt0aaOiuilRCN1HGAgXWoqND7B69x1rg7OwZc&dib_tag=se&keywords=5x11%2Bflanged%2Bbearing&qid=1724780488&sprefix=5x11%2Bflanged%2Bb%2Caps%2C116&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/shoulder_bolt_m4x30mm.png" style="width:100;">
      </td>
      <td align="left"> Alloy Steel Shoulder Screws <br>
        &#8960; 5mm x 30mm Shoulder, M4 x 0.7mm Thread</td>
      <td>6</td>
      <td>3.03</td>
      <td>18.18</td>
      <td>
        <a href="https://www.mcmaster.com/92981A055/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/lock_nut_m4.png" style="width:100;">
      </td>
      <td align="left">M4 x 0.7mm Locknut <br>
        (package of 100, 6 required)
      </td>
      <td>1</td>
      <td>5.57</td>
      <td>5.57</td>
      <td>
        <a href="https://www.mcmaster.com/90576A103/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/thread_m3.png" style="width:100;"></td>
      <td align="left">
        Heat Set Insert <br>
        M3 x 0.5mm Thread Size, 3.8 mm Installed Length <br>
        (Package of 100, 4 required)
      </td>
      <td>1</td>
      <td>20.44</td>
      <td>20.44</td>
      <td>
        <a href="https://www.mcmaster.com/94180A331/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/bolt_m3_30.png" style="width:100;">
      </td>
      <td align="left">
        M3 x 30mm Long Socket Head Screws <br>
        (pack of 50, 4 required)</td>
      <td>1</td>
      <td>13.68</td>
      <td>13.68</td>
      <td>
        <a href="https://www.mcmaster.com/91290A130/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/bolt_m3_12.png" style="width:100;">
      </td>
      <td align="left">
        M3 x 12mm Long Socket Head Screws <br>
        (pack of 100, 10 required)
      </td>
      <td>1</td>
      <td>11.29</td>
      <td>11.29</td>
      <td>
        <a href="https://www.mcmaster.com/91290A117/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/nut_m3.png" style="width:100;"></td>
      <td align="left">
        M3 x 0.5 mm Nut <br>
        (packge of 100, 10 required)
      </td>
      <td>1</td>
      <td>2.81</td>
      <td>2.81</td>
      <td>
        <a href="https://www.mcmaster.com/90591A250/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/bolt_m6_14.png" style="width:100;">
      </td>
      <td align="left">
        M6 x 14mm Long Socket Head Screws <br>
        (pack of 100, 4 required)
      </td>
      <td>1</td>
      <td>19.69</td>
      <td>19.69</td>
      <td>
        <a href="https://www.mcmaster.com/91290A319/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/nut_m6.png" style="width:100;">
      </td>
      <td align="left">
        M6 x 1mm Nut <br>
        (packge of 100, 4 required)
      </td>
      <td>1</td>
      <td>x.xx</td>
      <td>x.xx</td>
      <td>
        <a href="https://www.mcmaster.com/90591A151/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/bolt_m2_5_8.png" style="width:100;">
      </td>
      <td align="left">
        M2.5 x 8mm Long Socket Head Screws <br>
        (packge of 50, 2 required)
      </td>
      <td>1</td>
      <td>11.42</td>
      <td>11.42</td>
      <td>
        <a href="https://www.mcmaster.com/91290A102/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/bolt_m2_5_6.png" style="width:100;">
      </td>
      <td align="left">
        M2.5 x 6mm Long Socket Head Screws <br>
        (packge of 50, 8 required)
      </td>
      <td>1</td>
      <td>11.56</td>
      <td>11.56</td>
      <td>
        <a href="https://www.mcmaster.com/91290A101/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <img src="./src/figure/off-the-shelf/bolt_m2_6.png" style="width:100;"></td>
      <td align="left">
        M2 x 6mm Long Socket Head Screws <br>
        (packge of 100, 16-32 required)
      </td>
      <td>1</td>
      <td>15.68</td>
      <td>15.68</td>
      <td>
        <a href="https://www.mcmaster.com/91290A013/">
          <i class="fa-solid fa-link"></i>
        </a>
      </td>
    </tr>
    <!-- Add more rows as needed -->
  </table>

  </td>
  </tr>
</table>


<hr>

<table align=center width=800px>
  <tr>
    <td>

<h2> 3D-printing Parts</h2>

<table class="bom_table">
    <thead>
    <tr>
        <th></th>
        <th>Item</th>
        <th>Material</th>
        <th>Quantity</th>
        <th>File</th>
    </tr>
    </thead>
    <tr>
        <td>
          <img src="./src/figure/gripper/Base.png" style="width:100;">
        </td>
        <td>Base</td>
        <td>PLA</td>
        <td>1</td>
        <td>
          <a href="./src/stl/gripper/Base.STL" download>
            <i class="fa-solid fa-download"></i>
          </a>
        </td>
    </tr>
    <tr>
        <td>
          <img src="./src/figure/gripper/Dynamixel_Mount.png" style="width:100;">
        </td>
        <td>Dynamixel Mount</td>
        <td>PLA</td>
        <td>2</td>
        <td>
          <a href="./src/stl/gripper/Dynamixel_Mount.STL" download>
            <i class="fa-solid fa-download"></i>
          </a>
        </td>
    </tr>
    <tr>
        <td>
          <img src="./src/figure/gripper/Finger_Link.png" style="width:100;">
        </td>
        <td>Finger Link</td>
        <td>PLA</td>
        <td>2</td>
        <td>
          <a href="./src/stl/gripper/Finger_Link.STL" download>
            <i class="fa-solid fa-download"></i>
          </a>
        </td>
    </tr>
    <tr>
        <td>
          <img src="./src/figure/gripper/Lower_Link.png" style="width:100;">
        </td>
        <td>Lower Link</td>
        <td>PLA</td>
        <td>2</td>
        <td>
          <a href="./src/stl/gripper/Lower_Link.STL" download>
            <i class="fa-solid fa-download"></i>
          </a>
        </td>
    </tr>
    <tr>
        <td>
          <img src="./src/figure/gripper/Upper_Link_Half.png" style="width:100;">
        </td>
        <td>Upper Link Half</td>
        <td>PLA</td>
        <td>4</td>
        <td>
          <a href="./src/stl/gripper/Upper_Link_Half.STL" download>
            <i class="fa-solid fa-download"></i>
          </a>
        </td>
    </tr>
    <tr>
        <td>
          <img src="./src/figure/gripper/Finger_Tip.png" style="width:100;">
        </td>
        <td>Finger Tip</td>
        <td>TPU 95A</td>
        <td>2</td>
        <td>
          coming<br>
          soon
        </td>
    </tr>
    <!-- Add more rows as needed -->
</table>

<h2>3D-printing Handles</h2>

<table class="bom_table">
  <thead>
    <tr>
        <th></th>
        <th>Item</th>
        <th>Material</th>
        <th>Quantity</th>
        <th>File</th>
    </tr>
  </thead>
    <tr>
        <td>
          <img src="./src/figure/handle/Human_Handle.png" style="width:100;">
        </td>
        <td>Human Handle</td>
        <td>PLA</td>
        <td>1</td>
        <td>
          <a href="./src/stl/gripper/Human_Handle.STL" download>
            <i class="fa-solid fa-download"></i>
          </a>
        </td>
    </tr>
    <tr>
        <td>
          <img src="./src/figure/handle/Spot_Handle.png" style="width:100;">
        </td>
        <td>Spot Handle</td>
        <td>PLA</td>
        <td>1</td>
        <td>
          <a href="./src/stl/gripper/Spot_Handle.STL" download>
            <i class="fa-solid fa-download"></i>
          </a>
        </td>
    </tr>
    <tr>
        <td>
          <img src="./src/figure/handle/Panda_Handle_1.png" style="width:100;">
        </td>
        <td>Panda Handle 1</td>
        <td>PLA</td>
        <td>1</td>
        <td>
          <a href="./src/stl/handle/Panda_Handle_1.STL" download>
            <i class="fa-solid fa-download"></i>
          </a>
        </td>
    </tr>
    <tr>
        <td>
          <img src="./src/figure/handle/Panda_Handle_2.png" style="width:100;">
        </td>
        <td>Panda Handle 2</td>
        <td>PLA</td>
        <td>1</td>
        <td>
          <a href="./src/stl/handle/Panda_Handle_2.STL" download>
            <i class="fa-solid fa-download"></i>
          </a>
        </td>
    </tr>
    <!-- Add more rows as needed -->
</table>

  </td>
  </tr>
</table>

<hr>
<center><h1>Citation</h1></center>

<table align=center width=800px>
  <tr>
    <td>
    <!-- <left> -->
    <pre><code style="display:block; overflow-x: auto">
      @misc{seo2024legato,
        title={LEGATO: Cross-Embodiment Visual Imitation Using a Grasping Tool},
        author={Seo, Mingyo and Park, H. Andy and Yuan, Shenli and Zhu, Yuke and
          and Sentis, Luis},
        year={2024}
        eprint={XXXX.XXXXXX},
        archivePrefix={arXiv},
        primaryClass={cs.RO}
      }
    </code></pre>
    <!-- </left> -->
    </td>
  </tr>
</table>

<div class="page-width-background">
<div style="height: 4px;"></div>
<center><h2 align="center">Acknowledgement</h2></center>
<table align=center width=800px>
  <tr>
    <td> 
      <p align="justify" width="20%">
        This work was conducted during Mingyo Seo's internship at the AI Institute. We thank Rutav Shah and Minkyung Kim for providing feedback on this manuscript. We thank Dr. Osman Dogan Yirmibesoglu for designing the fin ray style compliant fingers and helping with hardware prototyping. We thank Mitchell Pryor and Fabian Parra for their support with the real Spot demonstration. We acknowledge the support of the AI Institute and the Office of Naval Research (N00014-22-1-2204).
      </p>
    </td>
  </tr>
</table>
<div style="height: 16px;"></div>
</div>