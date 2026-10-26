# Practical Hardware Tools

Seven free browser calculators for hardware planning, with worked examples, scenario comparisons and CSV export. No account or installation is required.

**[Open the free hardware calculators](https://nagimoon2000-crypto.github.io/practical-hardware-tools/?utm_source=github&utm_medium=readme&utm_campaign=discovery)**

## Choose the question you need to answer

| Engineering question | Free tool | What it calculates |
| --- | --- | --- |
| How much does sleep current change my sensor's runtime? | [IoT battery life calculator](https://nagimoon2000-crypto.github.io/practical-hardware-tools/battery-life-calculator/?utm_source=github&utm_medium=readme&utm_campaign=discovery) | Weighted average current and estimated battery runtime over a repeating cycle |
| What exposure keeps a moving object within a blur allowance? | [Camera motion blur calculator](https://nagimoon2000-crypto.github.io/practical-hardware-tools/camera-motion-blur-calculator/?utm_source=github&utm_medium=readme&utm_campaign=discovery) | Lateral image motion in pixels and an exposure limit |
| Will a capacitor bank keep the load powered long enough? | [Supercapacitor hold-up calculator](https://nagimoon2000-crypto.github.io/practical-hardware-tools/supercapacitor-hold-up-calculator/?utm_source=github&utm_medium=readme&utm_campaign=discovery) | Usable energy across a voltage window and idealized hold-up time |
| How much recording storage do my cameras need? | [Camera storage calculator](https://nagimoon2000-crypto.github.io/practical-hardware-tools/camera-storage-calculator/?utm_source=github&utm_medium=readme&utm_campaign=discovery) | Decimal GB/TB from encoded bitrate, camera count and retention |
| Why does a 20 ms inference not deliver 50 FPS? | [Edge AI FPS calculator](https://nagimoon2000-crypto.github.io/practical-hardware-tools/edge-ai-fps-calculator/?utm_source=github&utm_medium=readme&utm_campaign=discovery) | Serial stage latency, estimated FPS and frame-budget margin |
| How long should I record vibration for 1 Hz FFT bins? | [Vibration FFT planner](https://nagimoon2000-crypto.github.io/practical-hardware-tools/vibration-fft-calculator/?utm_source=github&utm_medium=readme&utm_campaign=discovery) | Record duration, bin spacing and Nyquist frequency |
| Do the pull-ups on multiple I2C sensor boards become too strong in parallel? | [I2C pull-up resistor calculator](https://nagimoon2000-crypto.github.io/practical-hardware-tools/i2c-pullup-resistor-calculator/?utm_source=github&utm_medium=readme&utm_campaign=discovery) | Rise-time and sink-current bounds, resistor tolerance and parallel pull-ups |

## Start with a worked guide

[Browse six practical question-to-tool routes](https://moons66.wordpress.com/2026/10/26/start-here-find-your-free-hardware-calculator-and-worked-guide/?utm_source=github&utm_medium=readme&utm_campaign=guide_directory): battery life, CCTV storage, I2C pull-ups, motion blur, backup power and Edge AI FPS. Each route links a worked guide, its free calculator and an optional related Payhip resource.

[Follow new guides through RSS](https://moons66.wordpress.com/feed/). Copy this feed address into your RSS reader; no email address is needed for this option.

## Try a concrete example

1. Open the Edge AI calculator.
2. Start with 10 ms capture, 5 ms preprocessing, 20 ms inference and 5 ms postprocessing.
3. The serial total is 40 ms, corresponding to 25 FPS, below a 30 FPS target.
4. Select the **10 ms inference** scenario. The total becomes 30 ms, or about 33.33 FPS.
5. Export the CSV if you want to retain the calculation.

These numbers illustrate arithmetic, not a device benchmark. Overlapping pipeline stages require a separate throughput model.

Calculator pages explain their assumptions and model limits. Use the available examples and scenarios as starting points, then replace inputs with measurements from your hardware.

## Use the results responsibly

- Measure inputs at the relevant boundary. For a battery budget, battery-terminal current includes effects that a downstream rail measurement may miss.
- Use consistent units. Camera bitrate is in Mbps; storage totals use decimal units.
- Treat calculated outputs as estimates. Battery aging, capacitor ESR, image-system geometry and pipeline overlap can require more detailed models.
- Validate assumptions against your hardware. These pages do not provide certification, device benchmarks or manufacturer endorsement.

## Privacy

Calculator inputs are processed in the browser. Optional Google Analytics remains off until you allow it. When enabled, it records page visits and interaction events, not calculator input values or results. Hosting providers may process ordinary access logs.

## Need a structured measurement record?

The calculators are free to use. Separate paid XLSX workbooks provide planning and measurement-recording workflows.

[Compare the battery and Edge AI workbooks, limits and free starter files](https://nagimoon2000-crypto.github.io/practical-hardware-tools/hardware-spreadsheet-guides/?utm_source=github&utm_medium=readme&utm_campaign=discovery).

Purchasing a workbook is not required to use the calculators.

## Report a calculation problem

[Open an issue](https://github.com/nagimoon2000-crypto/practical-hardware-tools/issues/new) with:

- The calculator URL.
- Non-confidential example inputs and units.
- The observed output and your expected result, with the formula or reference.
- Browser/device information if the problem is visual or interactive.

Please do not include confidential designs, customer data or credentials. Reports help distinguish a formula error from a limitation of the simplified model.

## Share a useful tool

Link to the calculator that answers the specific engineering question, rather than only the home page. Each tool works directly in the browser and includes its own explanation.

Prepared with AI assistance. Examples are illustrative; engineering validation remains the user's responsibility.