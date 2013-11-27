# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.ants.resampling import WarpTimeSeriesImageMultiTransform
def test_WarpTimeSeriesImageMultiTransform_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    invert_affine=dict(),
    reslice_by_header=dict(argstr='--reslice-by-header',
    ),
    tightest_box=dict(xor=['reference_image'],
    argstr='--tightest-bounding-box',
    ),
    out_postfix=dict(argstr='%s',
    usedefault=True,
    ),
    use_nearest=dict(argstr='--use-NN',
    ),
    args=dict(argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    reference_image=dict(xor=['tightest_box'],
    argstr='-R %s',
    ),
    input_image=dict(copyfile=True,
    mandatory=True,
    argstr='%s',
    ),
    use_bspline=dict(argstr='--use-Bspline',
    ),
    transformation_series=dict(copyfile=False,
    mandatory=True,
    argstr='%s',
    ),
    dimension=dict(position=1,
    usedefault=True,
    argstr='%d',
    ),
    )
    inputs = WarpTimeSeriesImageMultiTransform.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_WarpTimeSeriesImageMultiTransform_outputs():
    output_map = dict(output_image=dict(),
    )
    outputs = WarpTimeSeriesImageMultiTransform.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value