# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.epi import EddyCorrect
def test_EddyCorrect_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(hash_files=False,
    genfile=True,
    position=1,
    argstr='%s',
    ),
    args=dict(argstr='%s',
    ),
    ref_num=dict(position=2,
    mandatory=True,
    argstr='%d',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(position=0,
    mandatory=True,
    argstr='%s',
    ),
    output_type=dict(),
    )
    inputs = EddyCorrect.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_EddyCorrect_outputs():
    output_map = dict(eddy_corrected=dict(),
    )
    outputs = EddyCorrect.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value