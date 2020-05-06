<div id="observablehq-18777612"></div>
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
import define from "https://api.observablehq.com/@d3/box-plot.js?v=3";
const inspect = Inspector.into("#observablehq-18777612");
(new Runtime).module(define, name => (name === "chart") && inspect());
</script>
