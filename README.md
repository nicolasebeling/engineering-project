# Application of HyperMesh Certification to Inter-Rivet Buckling

This project aims to simplify the calculation of the margin of safety against inter-rivet buckling using the [Altair HyperMesh Certification](https://2023.help.altair.com/2023.1/hwdesktop/hwx/topics/pre_processing/aerospace/certification_unity_c.htm) framework.

The provided code and documentation have been tested in version `2023.1` but should work in later versions too.

:exclamation: Everything that follows is work in progress. :exclamation:

## Workflow for Metallic Structures :hammer_and_wrench:

Note that the implemented HSB formula is only applicable to load cases without transverse loads with respect to the direction of the fastener row. If there is a tensile transverse load, the actual 
reserve factor will be higher. If there is a compressive transverse load, the actual reserve factor will be lower.

1. Import the provided library `irb_library.xml`.
2. Create a structural property of type `Panel_metallic` and add the following metadata:
   - Fastener pitch ` s`
   - Fastener row direction as `x`, `y`, `z` components
   - Clamping factor `C`
3. Create a design point set.
4. Create structural elements (design points) of type `Panel_metallic`.
5. Run the method provided method on the previously created design point set.

## Testing

All files have been tested on the following models and results:
- `Altair_Wingddp_start.hm` and `Altair_Wing_LC101_Take_Off_p27deg_Hot_Step1.op2` (part of a workshop by Altair, not available here)

## Open Questions

- Are there more precise formulas for inter-rivet buckling than the ones presented in the HSB? These formulas neglect transverse forces (i.e. assume there are none).
- Is there a simpler way to get the fastener pitch than entering it manually as metadata?
- Not important but confusing: Why is Design Point abbreviated as DDP instead of DP?

## Abbreviations :spiral_notepad:
- `irb` = inter-rivet buckling
- `cr` = critical
- `sigma` = stress in N/mm<sup>2<sup/>
- `n` = force flow in N/mm