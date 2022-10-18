/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44AOO.h
 *
 * Code generated for Simulink model 'Group44AOO'.
 *
 * Model version                  : 1.6
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Mon Oct 17 18:23:59 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_Group44AOO_h_
#define RTW_HEADER_Group44AOO_h_
#ifndef Group44AOO_COMMON_INCLUDES_
#define Group44AOO_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_PWM.h"
#endif                                 /* Group44AOO_COMMON_INCLUDES_ */

#include "Group44AOO_types.h"
#include <stddef.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* Block signals (default storage) */
typedef struct {
  real_T dutyCycle;                    /* '<S1>/Chart' */
} B_Group44AOO_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_DigitalWrite_Grou_T obj; /* '<Root>/Z_VENT_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_l;/* '<Root>/Z_ATR_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_g;/* '<Root>/VENT_PACE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_h;/* '<Root>/VENT_GND_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_h0;/* '<Root>/PACE_GND_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_lf;/* '<Root>/PACE_CHARGE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_e;/* '<Root>/ATR_PACE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_l5;/* '<Root>/ATR_GND_CTRL' */
  freedomk64f_PWMOutput_Group44_T obj_b;/* '<Root>/PACING_REF_PWM' */
  uint32_T temporalCounter_i1;         /* '<S1>/Chart' */
  uint8_T is_c3_Group44AOO;            /* '<S1>/Chart' */
  uint8_T is_active_c3_Group44AOO;     /* '<S1>/Chart' */
} DW_Group44AOO_T;

/* Parameters (default storage) */
struct P_Group44AOO_T_ {
  real_T p_aPaceWidth_Value;           /* Expression: 4
                                        * Referenced by: '<Root>/p_aPaceWidth'
                                        */
  real_T p_lowrateInterval_Value;      /* Expression: 1000
                                        * Referenced by: '<Root>/p_lowrateInterval'
                                        */
  real_T p_aPaceAmp_Value;             /* Expression: 4
                                        * Referenced by: '<Root>/p_aPaceAmp'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_Group44AOO_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_Group44AOO_T Group44AOO_P;

/* Block signals (default storage) */
extern B_Group44AOO_T Group44AOO_B;

/* Block states (default storage) */
extern DW_Group44AOO_T Group44AOO_DW;

/* Model entry point functions */
extern void Group44AOO_initialize(void);
extern void Group44AOO_step(void);
extern void Group44AOO_terminate(void);

/* Real-time Model object */
extern RT_MODEL_Group44AOO_T *const Group44AOO_M;
extern volatile boolean_T stopRequested;
extern volatile boolean_T runModel;

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<Root>/Scope' : Unused code path elimination
 */

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'Group44AOO'
 * '<S1>'   : 'Group44AOO/Subsystem'
 * '<S2>'   : 'Group44AOO/Subsystem/Chart'
 */
#endif                                 /* RTW_HEADER_Group44AOO_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
