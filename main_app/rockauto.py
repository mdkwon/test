from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

ebay_type_dictionary = {'Crankshaft Position Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Crankshaft Position Sensor',
 'Fuel Injection Pressure Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Fuel Injection Pressure Sensor',
 'Fuel Level Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Fuel Level Sensor',
 'Knock (Detonation) Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Knock (Detonation) Sensor',
 'Manifold Air Pressure Sensor (MAP Sensor)': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Manifold Air Pressure Sensor (MAP Sensor)',
 'Mass Airflow Sensor (MAF Sensor)': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Mass Airflow Sensor (MAF Sensor)',
 'Oxygen Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Oxygen Sensor',
 'Throttle Position Sensor (TPS)': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Throttle Position Sensor (TPS)',
 'Wideband Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Wideband Sensor',
 'Battery Cable': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Battery Cable',
 'Battery Cap': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Battery Cap',
 'Battery Disconnect': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Battery Disconnect',
 'Battery Isolator': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Battery Isolator',
 'Bulk Battery Cable': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Bulk Battery Cable',
 'Cut-Off Switch': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Cut-Off Switch',
 'DC to DC Charger': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=DC to DC Charger',
 'Fuse': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Fuse',
 'Grounding Cable': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Grounding Cable',
 'Negative Battery Cable': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Negative Battery Cable',
 'Postive & Negative Battery Cables': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Postive & Negative Battery Cables',
 'Postive Battery Cable': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Postive Battery Cable',
 'Terminal': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Terminal',
 'Terminal Cleaner': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Terminal Cleaner',
 'Terminal Protector': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Terminal Protector',
 'Warmer': 'https://www.ebay.com/b/Car-Truck-Battery-Cables-Connectors/179847?Type=Warmer',
 'Coolant Bottle': 'https://www.ebay.com/b/Car-Truck-Radiators-Parts/33602?Type=Coolant Bottle',
 'Fan Shroud': 'https://www.ebay.com/b/Car-Truck-Radiators-Parts/33602?Type=Fan Shroud',
 'Mounting Bracket': 'https://www.ebay.com/b/Car-Truck-Radiators-Parts/33602?Type=Mounting Bracket',
 'Overflow Tank': 'https://www.ebay.com/b/Car-Truck-Radiators-Parts/33602?Type=Overflow Tank',
 'Radiator': 'https://www.ebay.com/b/Car-Truck-Radiators-Parts/33602?Type=Radiator',
 'Radiator Cap': 'https://www.ebay.com/b/Car-Truck-Radiators-Parts/33602?Type=Radiator Cap',
 'Radiator Hose': 'https://www.ebay.com/b/Car-Truck-Radiators-Parts/33602?Type=Radiator Hose',
 'Connecting Rod': 'https://www.ebay.com/b/Car-Truck-Pistons-Rings-Rods-Parts/33623?Type=Connecting Rod',
 'Piston': 'https://www.ebay.com/b/Car-Truck-Pistons-Rings-Rods-Parts/33623?Type=Piston',
 'Piston Ring': 'https://www.ebay.com/b/Car-Truck-Pistons-Rings-Rods-Parts/33623?Type=Piston Ring',
 'Continuous Duty Solenoid': 'https://www.ebay.com/b/Car-Truck-Engine-Timing-Components/33625?Type=Continuous Duty Solenoid',
 'Oil Pump': 'https://www.ebay.com/b/Car-Truck-Engine-Timing-Components/33625?Type=Oil Pump',
 'Timing Belt': 'https://www.ebay.com/b/Car-Truck-Engine-Timing-Components/33625?Type=Timing Belt',
 'Timing Belt Kit': 'https://www.ebay.com/b/Car-Truck-Engine-Timing-Components/33625?Type=Timing Belt Kit',
 'Timing Chain': 'https://www.ebay.com/b/Car-Truck-Engine-Timing-Components/33625?Type=Timing Chain',
 'Timing Gear': 'https://www.ebay.com/b/Car-Truck-Engine-Timing-Components/33625?Type=Timing Gear',
 'Water Pump': 'https://www.ebay.com/b/Car-Truck-Engine-Timing-Components/33625?Type=Water Pump',
 'Capsule Cover': 'https://www.ebay.com/b/Car-Covers/50456?Type=Capsule Cover',
 'Disposable Cover': 'https://www.ebay.com/b/Car-Covers/50456?Type=Disposable Cover',
 'Full Coverage Cover': 'https://www.ebay.com/b/Car-Covers/50456?Type=Full Coverage Cover',
 'Portable Garage Cover': 'https://www.ebay.com/b/Car-Covers/50456?Type=Portable Garage Cover',
 'Roof Cover': 'https://www.ebay.com/b/Car-Covers/50456?Type=Roof Cover',
 'Tire Cover': 'https://www.ebay.com/b/Car-Truck-Tire-Accessories/33746?Type=Tire Cover',
 'Truck Tarp': 'https://www.ebay.com/b/Car-Covers/50456?Type=Truck Tarp',
 'Windshield Cover': 'https://www.ebay.com/b/Car-Covers/50456?Type=Windshield Cover',
 'Door Hinge': 'https://www.ebay.com/b/Car-Truck-Door-Hinge-Conversion-Kits/179849?Type=Door Hinge',
 'Hood Hinge': 'https://www.ebay.com/b/Car-Truck-Door-Hinge-Conversion-Kits/179849?Type=Hood Hinge',
 'Trunk Hinge': 'https://www.ebay.com/b/Car-Truck-Door-Hinge-Conversion-Kits/179849?Type=Trunk Hinge',
 'Door Handle': 'https://www.ebay.com/b/Car-Truck-Interior-Door-Handles/179848?Type=Door Handle',
 'Door Handle & Bezel Assembly': 'https://www.ebay.com/b/Car-Truck-Interior-Door-Handles/179848?Type=Door Handle & Bezel Assembly',
 'Door Handle Bezel': 'https://www.ebay.com/b/Car-Truck-Interior-Door-Handles/179848?Type=Door Handle Bezel',
 'Fender': 'https://www.ebay.com/b/Car-Truck-Fenders/33644?Type=Fender',
 'Fender Filler': 'https://www.ebay.com/b/Car-Truck-Fenders/33644?Type=Fender Filler',
 'Fender Flares': 'https://www.ebay.com/b/Car-Truck-Fenders/33644?Type=Fender Flares',
 'Fender Support': 'https://www.ebay.com/b/Car-Truck-Fenders/33644?Type=Fender Support',
 'Fender Trim': 'https://www.ebay.com/b/Car-Truck-Fenders/33644?Type=Fender Trim',
 'Door': 'https://www.ebay.com/b/Car-Truck-Locks-Hardware/33648?Type=Door',
 'Fuel Door/Cap': 'https://www.ebay.com/b/Car-Truck-Locks-Hardware/33648?Type=Fuel Door/Cap',
 'Tailgate': 'https://www.ebay.com/b/Car-Truck-Tailgates-Liftgates/33647?Type=Tailgate',
 'Toolbox': 'https://www.ebay.com/b/Car-Truck-Locks-Hardware/33648?Type=Toolbox',
 'Accessories': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Accessories',
 'Boat Loader': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Boat Loader',
 'Carrier Rack': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Carrier Rack',
 'Cross Bar': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Cross Bar',
 'Fixpoint Roof Rack': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Fixpoint Roof Rack',
 'Kayak Carrier': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Kayak Carrier',
 'Ladder Rack': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Ladder Rack',
 'Rain Gutter Roof Rack': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Rain Gutter Roof Rack',
 'Roof Basket': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Roof Basket',
 'Roof Pod': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Roof Pod',
 'Roof Rail Rack': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Roof Rail Rack',
 'Side Bars': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Side Bars',
 'Ski/Snowboard': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Ski/Snowboard',
 'Soft Roof Rack': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Soft Roof Rack',
 'Surfboard': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Surfboard',
 'T-Tracks Roof Rack': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=T-Tracks Roof Rack',
 'Universal Roof Rack': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Universal Roof Rack',
 'Wheelchair': 'https://www.ebay.com/b/Car-Truck-Racks/33651?Type=Wheelchair',
 'Hard Top': 'https://www.ebay.com/b/Car-Truck-Sunroofs-Hard-Tops-Soft-Tops/33652?Type=Hard Top',
 'Moonroof': 'https://www.ebay.com/b/Car-Truck-Sunroofs-Hard-Tops-Soft-Tops/33652?Type=Moonroof',
 'Soft Top': 'https://www.ebay.com/b/Car-Truck-Sunroofs-Hard-Tops-Soft-Tops/33652?Type=Soft Top',
 'Sunroof': 'https://www.ebay.com/b/Car-Truck-Sunroofs-Hard-Tops-Soft-Tops/33652?Type=Sunroof',
 'Visor': 'https://www.ebay.com/b/Car-Truck-Sunroofs-Hard-Tops-Soft-Tops/33652?Type=Visor',
 'Cargo Door': 'https://www.ebay.com/b/Car-Truck-Tailgates-Liftgates/33647?Type=Cargo Door',
 'Extender': 'https://www.ebay.com/b/Car-Truck-Tailgates-Liftgates/33647?Type=Extender',
 'Hatch': 'https://www.ebay.com/b/Car-Truck-Tailgates-Liftgates/33647?Type=Hatch',
 'Liftgate': 'https://www.ebay.com/b/Car-Truck-Tailgates-Liftgates/33647?Type=Liftgate',
 'Net': 'https://www.ebay.com/b/Car-Truck-Tailgates-Liftgates/33647?Type=Net',
 'Struts': 'https://www.ebay.com/b/Car-Truck-Tailgates-Liftgates/33647?Type=Struts',
 'Tailgate Tent': 'https://www.ebay.com/b/Car-Truck-Tailgates-Liftgates/33647?Type=Tailgate Tent',
 'Washer Pump': 'https://www.ebay.com/b/Car-Truck-Windshield-Wiper-Systems/33657?Type=Washer Pump',
 'Wiper Arm': 'https://www.ebay.com/b/Car-Truck-Windshield-Wiper-Systems/33657?Type=Wiper Arm',
 'Wiper Motor': 'https://www.ebay.com/b/Car-Truck-Windshield-Wiper-Systems/33657?Type=Wiper Motor',
 'Wiper Nozzle': 'https://www.ebay.com/b/Car-Truck-Windshield-Wiper-Systems/33657?Type=Wiper Nozzle',
 'Wiper Pulse Board': 'https://www.ebay.com/b/Car-Truck-Windshield-Wiper-Systems/33657?Type=Wiper Pulse Board',
 'Wiper Refills': 'https://www.ebay.com/b/Car-Truck-Windshield-Wiper-Systems/33657?Type=Wiper Refills',
 'Electrical': 'https://www.ebay.com/b/Car-Truck-Oil-Pressure-Gauges/33676?Type=Electrical',
 'Mechanical': 'https://www.ebay.com/b/Car-Truck-Oil-Pressure-Gauges/33676?Type=Mechanical',
 'Ceramic Film': 'https://www.ebay.com/b/Car-Truck-Window-Tint/63689?Type=Ceramic Film',
 'Dyed Window Film': 'https://www.ebay.com/b/Car-Truck-Window-Tint/63689?Type=Dyed Window Film',
 'Hybrid Tinting Film': 'https://www.ebay.com/b/Car-Truck-Window-Tint/63689?Type=Hybrid Tinting Film',
 'Metalized Window Film': 'https://www.ebay.com/b/Car-Truck-Window-Tint/63689?Type=Metalized Window Film',
 'Glow Plug': 'https://www.ebay.com/b/Car-Truck-Spark-Plugs-Glow-Plugs/33693?Type=Glow Plug',
 'Spark Plug': 'https://www.ebay.com/b/Car-Truck-Spark-Plugs-Glow-Plugs/33693?Type=Spark Plug',
 'Door Handle Spring': 'https://www.ebay.com/b/Car-Truck-Interior-Door-Handles/179848?Type=Door Handle Spring',
 'Door Pull Strap': 'https://www.ebay.com/b/Car-Truck-Interior-Door-Handles/179848?Type=Door Pull Strap',
 'Blind Spot Mirror': 'https://www.ebay.com/b/Car-Truck-Interior-Mirrors/33699?Type=Blind Spot Mirror',
 'Rear View': 'https://www.ebay.com/b/Car-Truck-Interior-Mirrors/33699?Type=Rear View',
 'Accelerator': 'https://www.ebay.com/b/Car-Truck-Pedals-Pads/33700?Type=Accelerator',
 'Brake': 'https://www.ebay.com/b/Car-Truck-Pedals-Pads/33700?Type=Brake',
 'Clutch': 'https://www.ebay.com/b/Car-Truck-Pedals-Pads/33700?Type=Clutch',
 'Emergency Brake': 'https://www.ebay.com/b/Car-Truck-Pedals-Pads/33700?Type=Emergency Brake',
 'Foot Rest': 'https://www.ebay.com/b/Car-Truck-Pedals-Pads/33700?Type=Foot Rest',
 'Rear Window': 'https://www.ebay.com/b/Car-Truck-Window-Motors-Parts/33706?Type=Rear Window',
 'Side Window': 'https://www.ebay.com/b/Car-Truck-Window-Motors-Parts/33706?Type=Side Window',
 'Sliding Window': 'https://www.ebay.com/b/Car-Truck-Window-Motors-Parts/33706?Type=Sliding Window',
 'Window Regulator': 'https://www.ebay.com/b/Car-Truck-Window-Motors-Parts/33706?Type=Window Regulator',
 'Windscreen': 'https://www.ebay.com/b/Car-Truck-Window-Motors-Parts/33706?Type=Windscreen',
 'Light Bar': 'https://www.ebay.com/b/Car-Truck-Light-Bars/184669/bn?Type=Light Bar',
 'Light Bar Mount': 'https://www.ebay.com/b/Car-Truck-Light-Bars/184669/bn?Type=Light Bar Mount',
 'Foldable Steering Wheel Lock': 'https://www.ebay.com/b/Car-Steering-Wheel-Locks/184628/bn?Type=Foldable Steering Wheel Lock',
 'Full Face Steering Wheel Lock': 'https://www.ebay.com/b/Car-Steering-Wheel-Locks/184628/bn?Type=Full Face Steering Wheel Lock',
 'Pedal to Steering Wheel Lock': 'https://www.ebay.com/b/Car-Steering-Wheel-Locks/184628/bn?Type=Pedal to Steering Wheel Lock',
 'Twin Hooks Steering Wheel Lock': 'https://www.ebay.com/b/Car-Steering-Wheel-Locks/184628/bn?Type=Twin Hooks Steering Wheel Lock',
 'Axle': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Axle',
 'Bearing': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Bearing',
 'Carrier': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Carrier',
 'Cover': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Cover',
 'Differential': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Differential',
 'Gasket': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Gasket',
 'Gear': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Gear',
 'Pinion': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Pinion',
 'Posi Differential': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Posi Differential',
 'Seal': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Seal',
 'Traction Unit': 'https://www.ebay.com/b/Car-Truck-Differentials-Parts/33731?Type=Traction Unit',
 'Flexplate': 'https://www.ebay.com/b/Car-Truck-Flywheels-Flexplates-Parts/33732?Type=Flexplate',
 'Flywheel': 'https://www.ebay.com/b/Car-Truck-Flywheels-Flexplates-Parts/33732?Type=Flywheel',
 'Housing': 'https://www.ebay.com/b/Car-Truck-Flywheels-Flexplates-Parts/33732?Type=Housing',
 'Clips': 'https://www.ebay.com/b/Car-Truck-Universal-Joints-Driveshafts/33738?Type=Clips',
 'Driveshaft': 'https://www.ebay.com/b/Car-Truck-Universal-Joints-Driveshafts/33738?Type=Driveshaft',
 'Grease': 'https://www.ebay.com/b/Car-Truck-Universal-Joints-Driveshafts/33738?Type=Grease',
 'Great Plug': 'https://www.ebay.com/b/Car-Truck-Universal-Joints-Driveshafts/33738?Type=Great Plug',
 'Joint': 'https://www.ebay.com/b/Car-Truck-Universal-Joints-Driveshafts/33738?Type=Joint',
 'Snap Rings': 'https://www.ebay.com/b/Car-Truck-Universal-Joints-Driveshafts/33738?Type=Snap Rings',
 'Zerk Fitting': 'https://www.ebay.com/b/Car-Truck-Universal-Joints-Driveshafts/33738?Type=Zerk Fitting',
 'Air Pressure Warning Switch': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Air Pressure Warning Switch',
 'Control Unit': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Control Unit',
 'Module Connector': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Module Connector',
 'Programmable Sensor': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Programmable Sensor',
 'Programmable Sensor Service Kit': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Programmable Sensor Service Kit',
 'Programmer': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Programmer',
 'Receiver': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Receiver',
 'Remote Tire Pressure Monitor': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Remote Tire Pressure Monitor',
 'Sensor': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor',
 'Sensor Clip': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Clip',
 'Sensor Component Kit': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Component Kit',
 'Sensor Cradle': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Cradle',
 'Sensor Grommet': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Grommet',
 'Sensor Mounting Band': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Mounting Band',
 'Sensor Nut': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Nut',
 'Sensor Retrofit Kit': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Retrofit Kit',
 'Sensor Service Kit': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Service Kit',
 'Sensor Service Tool': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Service Tool',
 'Sensor Valve Assembly': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Sensor Valve Assembly',
 'Tire Pressure Warning Lamp Connector': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Tire Pressure Warning Lamp Connector',
 'Tire Reset Tool': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Tire Reset Tool',
 'Valve': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Valve',
 'Valve Kit': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Valve Kit',
 'Valve Stem Core': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Valve Stem Core',
 'Valve Tool': 'https://www.ebay.com/b/Car-Truck-Tire-Pressure-Monitor-Systems/179696?Type=Valve Tool',
 'Tire Deflator': 'https://www.ebay.com/b/Car-Truck-Tire-Accessories/33746?Type=Tire Deflator',
 'Tire Groover': 'https://www.ebay.com/b/Car-Truck-Tire-Accessories/33746?Type=Tire Groover',
 'Tire Inflator': 'https://www.ebay.com/b/Car-Truck-Tire-Accessories/33746?Type=Tire Inflator',
 'Tire Patch': 'https://www.ebay.com/b/Car-Truck-Tire-Accessories/33746?Type=Tire Patch',
 'Tire Patch Plug': 'https://www.ebay.com/b/Car-Truck-Tire-Accessories/33746?Type=Tire Patch Plug',
 'Tire Pressure Gauge': 'https://www.ebay.com/b/Car-Truck-Tire-Accessories/33746?Type=Tire Pressure Gauge',
 'Tire Repair Kit': 'https://www.ebay.com/b/Car-Truck-Tire-Accessories/33746?Type=Tire Repair Kit',
 'Chain Tensioner': 'https://www.ebay.com/b/Car-Truck-Tire-Chains/180090?Type=Chain Tensioner',
 'Link Chains': 'https://www.ebay.com/b/Car-Truck-Tire-Chains/180090?Type=Link Chains',
 'Traction Cables': 'https://www.ebay.com/b/Car-Truck-Tire-Chains/180090?Type=Traction Cables',
 'Lug Bolt': 'https://www.ebay.com/b/Car-Truck-Lug-Nuts-Accessories/33749?Type=Lug Bolt',
 'Lug Nut': 'https://www.ebay.com/b/Car-Truck-Lug-Nuts-Accessories/33749?Type=Lug Nut',
 'Lug Nut Cover': 'https://www.ebay.com/b/Car-Truck-Lug-Nuts-Accessories/33749?Type=Lug Nut Cover',
 'Spike Lug Nut': 'https://www.ebay.com/b/Car-Truck-Lug-Nuts-Accessories/33749?Type=Spike Lug Nut',
 'Wheel Lock': 'https://www.ebay.com/b/Car-Truck-Lug-Nuts-Accessories/33749?Type=Wheel Lock',
 'Knock Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Knock (Detonation) Sensor',
 'Detonation Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Knock (Detonation) Sensor',
 'Manifold Air Pressure Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Manifold Air Pressure Sensor (MAP Sensor)',
 'MAP': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Manifold Air Pressure Sensor (MAP Sensor)',
 'MAP Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Manifold Air Pressure Sensor (MAP Sensor)',
 'Mass Airflow Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Mass Airflow Sensor (MAF Sensor)',
 'MAF': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Mass Airflow Sensor (MAF Sensor)',
 'MAF Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Mass Airflow Sensor (MAF Sensor)',
 'TPS Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Throttle Position Sensor (TPS)',
 'TPS': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Throttle Position Sensor (TPS)',
 'Throttle Position Sensor': 'https://www.ebay.com/b/Car-Truck-Air-Intake-Fuel-Delivery-Sensors/33557?Type=Throttle Position Sensor (TPS)'}


def rockauto(query):
    session = HTMLSession()
    r = session.get('http://google.com/search?q=' + query)
    sleep(1)
    corrected_query = r.html.find('#fprsl')
    if not corrected_query:
        google_corrected_query = query
    else:
        google_corrected_query = corrected_query[0].text
    driver = webdriver.Chrome("C:/Users/Kwon/Downloads/chromedriver.exe")
    driver.get('http://rockauto.com/en/catalog')
    rockauto_search_box = driver.find_element_by_id("topsearchinput[input]")
    rockauto_search_box.send_keys(google_corrected_query)
    rockauto_search_box.send_keys(Keys.ENTER)
    sleep(5)
    curr_url = driver.current_url
    driver.close()
    r = session.get(curr_url)
    rock_auto_prices = r.html.find('.ra-formatted-amount.listing-total')
    rock_auto_cheapest_item_image = r.html.find('.listing-inline-image.listing-inline-image-thumb.listing-inline-image-border')
    rockauto_cheapest_item_image_absolute_link_address = 'http://rockauto.com' + rock_auto_cheapest_item_image[0].attrs['src']
    price1 = rock_auto_prices[0].text
    session.close()

    return [price1, curr_url, google_corrected_query, rockauto_cheapest_item_image_absolute_link_address]

def ebay(query, user_part_input_query):
    session = HTMLSession()
    r = session.get('http://google.com/search?q=' + query)
    sleep(1)
    corrected_query = r.html.find('#fprsl')
    r = session.get('http://google.com/search?q=' + user_part_input_query)
    sleep(1)
    corrected_part_input_query = r.html.find('#fprsl')
    if not corrected_query:
        google_corrected_query = query
    else:
        google_corrected_query = corrected_query[0].text
    driver = webdriver.Chrome("C:/Users/Kwon/Downloads/chromedriver.exe")
    if not corrected_part_input_query:
        length_user_input_word_count = len(user_part_input_query.split())
    else:
        length_user_input_word_count = len(corrected_part_input_query.split())

    string_to_be_matched_with_dictionary = " ".join(google_corrected_query.split()[-length_user_input_word_count:])
    for key in ebay_type_dictionary.keys():
        if key.lower() == string_to_be_matched_with_dictionary.lower():
            match_success_variable = ebay_type_dictionary[key]
            break
    if match_success_variable:
        driver.get(match_success_variable + '&_nkw=' + google_corrected_query + '&_sop=15&LH_BIN=1')
    else:
        driver.get('https://www.ebay.com/sch/i.html?_nkw=' + google_corrected_query + '&_sop=15&LH_BIN=1')
    sleep(5)
    curr_url = driver.current_url
    driver.close()
    r = session.get(curr_url)
    ebay_prices = r.html.find('.s-item__price')
    ebay_item_link = r.html.find('.s-item__link')[0]
    ebay_cheapest_item_absolute_link = ''
    for i in ebay_item_link.absolute_links:
        ebay_cheapest_item_absolute_link = i
    ebay_photo_links = r.html.find('.s-item__image-img')[0]
    img = ebay_photo_links.xpath('//img')[0]
    ebay_cheapest_item_photo_link = img.attrs['src']
    ebay_cheapest_item_price = ebay_prices[0].text
    session.close()

    return [ebay_cheapest_item_price, curr_url, google_corrected_query, ebay_cheapest_item_photo_link, ebay_cheapest_item_absolute_link]





