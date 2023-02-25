// Production of copper wire
const copperWirePerSecond = 30; // units per second
const copperWireMachines = copperWirePerSecond / copperWireSpeed;
const copperNeededPerSecond = copperWirePerSecond * copperWireCopper / copperWireIron;
const copperMachinesNeeded = copperNeededPerSecond / copperSpeed;

// Production of green circuits
const greenCircuitsPerSecond = 10;
const greenCircuitMachines = greenCircuitsPerSecond / greenCircuitSpeed;
const copperNeededPerSecondForGreen = greenCircuitsPerSecond * greenCircuitCopper;
const copperWireNeededPerSecondForGreen = copperNeededPerSecondForGreen * greenCircuitCopperWire;
const copperMachinesNeededForGreen = (copperNeededPerSecondForGreen + copperWireNeededPerSecondForGreen) / copperSpeed;

// Production of electronic circuits
const electronicCircuitsPerSecond = 2;
const electronicCircuitMachines = electronicCircuitsPerSecond / electronicCircuitSpeed;
const ironNeededPerSecondForElectronic = electronicCircuitsPerSecond * electronicCircuitIron;
const copperNeededPerSecondForElectronic = electronicCircuitsPerSecond * electronicCircuitCopper;
const copperWireNeededPerSecondForElectronic = copperNeededPerSecondForElectronic * electronicCircuitCopperWire;
const copperMachinesNeededForElectronic = (copperNeededPerSecondForElectronic + copperWireNeededPerSecondForElectronic) / copperSpeed;
const ironMachinesNeededForElectronic = ironNeededPerSecondForElectronic / ironSpeed;

// Linear programming constraints
// Copper production
// copperMachinesNeeded * copperSpeed >= copperNeededPerSecond
// copperMachinesNeededForGreen * copperSpeed >= copperNeededPerSecondForGreen
// copperMachinesNeededForElectronic * copperSpeed >= copperNeededPerSecondForElectronic
// Iron production
// ironMachinesNeededForElectronic * ironSpeed >= ironNeededPerSecondForElectronic
// Total number of machines
// copperWireMachines + copperMachinesNeeded + greenCircuitMachines + copperMachinesNeededForGreen +
//   electronicCircuitMachines + copperMachinesNeededForElectronic + ironMachinesNeededForElectronic <= maxMachines
