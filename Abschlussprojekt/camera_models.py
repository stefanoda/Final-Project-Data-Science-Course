# camera_models.py

camera_models = {
    'Canon': {
        'Full-Frame': [
            'Canon EOS R1',  # New flagship
            'Canon EOS R3',
            'Canon EOS R5',
            'Canon EOS R5 Mark II',
            'Canon EOS R5 C',
            'Canon EOS R6',
            'Canon EOS R6 Mark II',
            'Canon EOS R8',
            'Canon EOS R',
            'Canon EOS RP',
            'Canon EOS 5D',
            'Canon EOS 5D Mark II',
            'Canon EOS 5D Mark III',
            'Canon EOS 5D Mark IV',
            'Canon EOS 6D',
            'Canon EOS 6D Mark II',
            'Canon EOS 1D X',
            'Canon EOS 1D X Mark II',
            'Canon EOS 1D X Mark III'
        ],
        'APS-C': [
            'Canon EOS R7',
            'Canon EOS R10',
            'Canon EOS R50',
            'Canon EOS 90D',
            'Canon EOS 80D',
            'Canon EOS 77D',
            'Canon EOS 70D',
            'Canon EOS 60D',
            'Canon EOS 7D',
            'Canon EOS 7D Mark II',
            'Canon EOS 850D (Rebel T8i)',
            'Canon EOS 800D (Rebel T7i)',
            'Canon EOS 750D (Rebel T6i)',
            'Canon EOS 700D (Rebel T5i)',
            'Canon EOS 650D (Rebel T4i)',
            'Canon EOS 600D (Rebel T3i)',
            'Canon EOS 550D (Rebel T2i)',
            'Canon EOS 500D (Rebel T1i)',
            'Canon EOS 1300D (Rebel T6)',
            'Canon EOS 1200D (Rebel T5)',
            'Canon EOS 1100D (Rebel T3)'
        ],
        '1-inch': [
            'Canon PowerShot G5 X', 
            'Canon PowerShot G5 X Mark II', 
            'Canon PowerShot G7 X', 
            'Canon PowerShot G7 X Mark II',
            'Canon PowerShot G7 X Mark III',
            'Canon PowerShot G9 X',
            'Canon PowerShot G9 X Mark II'
        ],
        'Micro Four Thirds': [],
        'Medium Format': [],
        'Other': []
    },
    'Nikon': {
        'Full-Frame': [
            'Nikon Z9', 'Nikon Z8', 'Nikon Z7 II', 'Nikon Z7', 
            'Nikon Z6 III', 'Nikon Z6 II', 'Nikon Z6', 'Nikon Z5',
            'Nikon D6', 'Nikon D5', 'Nikon D850', 'Nikon D810', 
            'Nikon D780', 'Nikon D750', 'Nikon D610'
        ],
        'APS-C': [
            'Nikon Z fc', 'Nikon Z50', 'Nikon Z30',
            'Nikon D7500', 'Nikon D7200', 'Nikon D7100',
            'Nikon D5600', 'Nikon D5500', 'Nikon D5300', 'Nikon D3500', 'Nikon D3400'
        ],
        'Micro Four Thirds': [],
        'Medium Format': [],
        'Other': [
            'Nikon Coolpix P1000', 'Nikon Coolpix P950', 'Nikon Coolpix P900'],
    },
    'Sony': {
        'Full-Frame': [
            'Sony A7', 'Sony A7 II', 'Sony A7 III', 'Sony A7 IV', 'Sony A7R', 'Sony A7R II', 'Sony A7R III', 
            'Sony A7R IV', 'Sony A7R V', 'Sony A7S', 'Sony A7S II', 'Sony A7S III', 'Sony A7C', 'Sony A7C II',
            'Sony A9', 'Sony A9 II', 'Sony A1', 'Other'
        ],
        'APS-C': [
            'Sony Alpha 6000', 'Sony Alpha 6100', 'Sony Alpha 6300', 'Sony Alpha 6400', 
            'Sony Alpha 6500', 'Sony Alpha 6600', 'Sony Alpha 6700', 'Sony ZV-E10', 'Sony ZV-E10 II', 'Other'
        ],
        'Micro Four Thirds': [],  # Sony does not have Micro Four Thirds cameras
        'Medium Format': [],
        '1-inch': [
            'Sony RX100', 'Sony RX100 II', 'Sony RX100 III', 'Sony RX100 IV', 
            'Sony RX100 V', 'Sony RX100 VI', 'Sony RX100 VII', 
            'Sony RX10', 'Sony RX10 II', 'Sony RX10 III', 'Sony RX10 IV',
            'Sony ZV-1', 'Other'
        ],
        'Other': []
    },

    'Fujifilm': {
        'Full-Frame':[],
        'APS-C': ['Fujifilm X-Pro1', 'Fujifilm X-Pro2', 'Fujifilm X-Pro3',
        'Fujifilm X-T1', 'Fujifilm X-T2', 'Fujifilm X-T3', 'Fujifilm X-T4', 'Fujifilm X-T5',
        'Fujifilm X-T10', 'Fujifilm X-T20', 'Fujifilm X-T30', 'Fujifilm X-T30 II',
        'Fujifilm X-H1', 'Fujifilm X-H2', 'Fujifilm X-H2S',
        'Fujifilm X-S10', 'Fujifilm X-S20',
        'Fujifilm X-E1', 'Fujifilm X-E2', 'Fujifilm X-E2s', 'Fujifilm X-E3', 'Fujifilm X-E4',
        'Fujifilm X-M1', 'Fujifilm X-A1', 'Fujifilm X-A2', 'Fujifilm X-A3', 'Fujifilm X-A5', 'Fujifilm X-A10', 'Fujifilm X-A20',
        'Fujifilm X100', 'Fujifilm X100S', 'Fujifilm X100T', 'Fujifilm X100F', 'Fujifilm X100V', 'Fujifilm X100VI',
        'Fujifilm XF10', 'Fujifilm X70'],

    'Micro Four Thirds': [],

    'Medium Format': [
        'Fujifilm GFX 50S', 'Fujifilm GFX 50S II', 'Fujifilm GFX 50R',
        'Fujifilm GFX 100', 'Fujifilm GFX 100S', 'Fujifilm GFX 100 II'
    ],
    
    'Other': [
        'Fujifilm X10', 'Fujifilm X20', 'Fujifilm X30', 
        'Fujifilm XQ1', 'Fujifilm XQ2', 
        'Fujifilm XF1', 
        'Fujifilm X-S1']
    },
    'Leica': {
        "Full-Frame": [
        "Leica M11", 
        "Leica M11 Monochrom", 
        "Leica M10", 
        "Leica M10-P", 
        "Leica M10-R", 
        "Leica M10 Monochrom", 
        "Leica M-A", 
        "Leica MP", 
        "Leica M6", 
        "Leica Q", 
        "Leica Q2", 
        "Leica Q2 Monochrom", 
        "Leica Q3", 
        "Leica SL2", 
        "Leica SL2-S", 
        "Leica SL3", 
        "Leica M10-P Reporter"
    ],
    "Medium Format": [
        "Leica S3"
    ],
    "APS-C": [
        "Leica CL", 
        "Leica TL2", 
        "Leica X Vario", 
        "Leica X-U (Typ 113)"
    ],
    "Micro Four Thirds": [
        "Leica D-Lux 7", 
        "Leica D-Lux 8"
    ],
    "1-inch": [
        "Leica C-Lux", 
        "Leica V-Lux 5"
    ],
    "Other": [
        # Keep this category for any additional models that don't fit into the main categories
    ]
    },
    'Olympus': {
        'Full-Frame': [],  # Olympus does not have Full-Frame cameras
        'APS-C': [],  # Olympus does not have APS-C cameras
        'Micro Four Thirds': ["Olympus OM-D E-M1X",
        "Olympus OM-D E-M1 Mark I",
        "Olympus OM-D E-M1 Mark II",
        "Olympus OM-D E-M1 Mark III",
        "Olympus OM-D E-M5 Mark I",
        "Olympus OM-D E-M5 Mark II",
        "Olympus OM-D E-M5 Mark III",
        "Olympus OM-D E-M10 Mark I",
        "Olympus OM-D E-M10 Mark II",
        "Olympus OM-D E-M10 Mark III",
        "Olympus OM-D E-M10 Mark IV",
        "Olympus PEN E-P7",
        "Olympus PEN E-PL10",
        "Olympus PEN E-PL9",
        "Olympus PEN E-PL8",
        "Olympus PEN-F",
        "OM System OM-1",
        "OM System OM-5"],
        'Medium Format': [],
        '1-inch': [],
        'Other': []
    
    },

    'Panasonic': {

        "Full-Frame": [
        "Panasonic Lumix S1",
        "Panasonic Lumix S1R",
        "Panasonic Lumix S1H",
        "Panasonic Lumix S5",
        "Panasonic Lumix S5 II",
        "Panasonic Lumix S5 IIX",
        "Panasonic Lumix S1M",
        "Panasonic Lumix S1RM"
    ],
    "Medium Format": [
        # Panasonic does not produce medium format cameras
    ],
    "APS-C": [
        # Panasonic does not produce APS-C cameras, mainly focuses on MFT and Full-Frame
    ],
    "Micro Four Thirds": [
        "Panasonic Lumix GH5",
        "Panasonic Lumix GH5 II",
        "Panasonic Lumix GH6",
        "Panasonic Lumix G9",
        "Panasonic Lumix G95",
        "Panasonic Lumix G100",
        "Panasonic Lumix GX9",
        "Panasonic Lumix GX85",
        "Panasonic Lumix GX8",
        "Panasonic Lumix G7",
        "Panasonic Lumix G85",
        "Panasonic Lumix G80",
        "Panasonic Lumix GF10",
        "Panasonic Lumix GF9",
        "Panasonic Lumix GF8",
        "Panasonic Lumix GF7",
        "Panasonic Lumix GM5",
        "Panasonic Lumix GM1"
    ],
    "1-inch": [
        "Panasonic Lumix LX100",
        "Panasonic Lumix LX100 II",
        "Panasonic Lumix TZ200",
        "Panasonic Lumix TZ100",
        "Panasonic Lumix FZ1000",
        "Panasonic Lumix FZ1000 II",
        "Panasonic Lumix FZ2000"
    ],
    "Other": [
        # Panasonic has no models in "Other" sensor categories.
    ]


    },

    'Pentax': {
        "Full-Frame": [
        "Pentax K-1",
        "Pentax K-1 Mark II"
    ],
    "Medium Format": [
        "Pentax 645Z"
    ],
    "APS-C": [
        "Pentax K-3",
        "Pentax K-3 II",
        "Pentax K-3 Mark III",
        "Pentax KP",
        "Pentax K-70",
        "Pentax K-S2",
        "Pentax K-S1",
        "Pentax K-50",
        "Pentax K-30",
        "Pentax K-5 II",
        "Pentax K-5 IIs",
        "Pentax K-5",
        "Pentax K-7"
    ],
    "Micro Four Thirds": [
        # Pentax does not produce Micro Four Thirds cameras.
    ],
    "1-inch": [
        # Pentax does not produce 1-inch sensor cameras.
    ],
    "Other": [
        # Pentax has no models in "Other" sensor categories.
    ]
    },
    'Hasselblad': {
        "Full-Frame": [
        # Hasselblad does not typically manufacture Full-Frame cameras.
    ],
    "Medium Format": [
        "Hasselblad X1D-50c",
        "Hasselblad X1D II 50C",
        "Hasselblad 907X 50C",
        "Hasselblad X2D 100C",
        "Hasselblad H6D-50c",
        "Hasselblad H6D-100c",
        "Hasselblad H5D-50c",
        "Hasselblad H5D-200c MS"
    ],
    "APS-C": [
        # Hasselblad does not produce APS-C sensor cameras.
    ],
    "Micro Four Thirds": [
        # Hasselblad does not produce Micro Four Thirds cameras.
    ],
    "1-inch": [
        # Hasselblad does not produce 1-inch sensor cameras.
    ],
    "Other": [
        # No other sensor categories for Hasselblad cameras.
    ]
    },
    'Phase One': {
        'Full-Frame': [],
        'APS-C': [],
        'Micro Four Thirds': [],  # Mamiya does not have Micro Four Thirds cameras
        'Medium Format': [
        'Phase One XF IQ4 150MP',
        'Phase One XF IQ4 100MP Trichromatic',
        'Phase One XF IQ4 100MP',
        'Phase One IQ3 100MP',
        'Phase One IQ3 100MP Trichromatic',
        'Phase One IQ3 80MP',
        'Phase One IQ2 60MP',
        'Phase One IQ1 50MP',
        'Phase One IQ1 40MP',
        'Phase One P65+',
        'Phase One P45+'],
        '1-inch': [],
        'Other': []
    },
    'Ricoh': {
        'Full-Frame': [],
        'APS-C': [
        'Ricoh GR',
        'Ricoh GR II',
        'Ricoh GR III',
        'Ricoh GR IIIx',    
        'Ricoh GR Digital IV'
    ],
        'Micro Four Thirds': [],  # Ricoh does not have Micro Four Thirds cameras
        'Medium Format': [],
        '1-inch': [],
        'Other': []
    },
    'Other':{'Other':[]}
}
    # Add more camera brands and their models here

