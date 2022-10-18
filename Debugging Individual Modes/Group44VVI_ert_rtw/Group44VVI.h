/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Group44VVI.h
 *
 * Code generated for Simulink model 'Group44VVI'.
 *
 * Model version                  : 1.2
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Mon Oct 17 16:30:25 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_Group44VVI_h_
#define RTW_HEADER_Group44VVI_h_
#ifndef Group44VVI_COMMON_INCLUDES_
#define Group44VVI_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_PWM.h"
#endif                                 /* Group44VVI_COMMON_INCLUDES_ */

#include "Group44VVI_types.h"
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
  real_T senseDutyCycle;               /* '<S1>/Chart' */
  boolean_T ATR_GND_CTRL;              /* '<S1>/Chart' */
  boolean_T ATR_PACE_CTRL;             /* '<S1>/Chart' */
  boolean_T PACE_CHARGE_CTRL;          /* '<S1>/Chart' */
  boolean_T PACE_GND_CTRL;             /* '<S1>/Chart' */
  boolean_T VENT_GND_CTRL;             /* '<S1>/Chart' */
  boolean_T VENT_PACE_CTRL;            /* '<S1>/Chart' */
  boolean_T Z_ATR_CTRL;                /* '<S1>/Chart' */
  boolean_T Z_VENT_CTRL;               /* '<S1>/Chart' */
} B_Group44VVI_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_DigitalRead_Group_T obj; /* '<Root>/VENT_CMP_DETECT' */
  freedomk64f_DigitalWrite_Grou_T obj_c;/* '<Root>/Z_VENT_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_m;/* '<Root>/Z_ATR_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_o;/* '<Root>/VENT_PACE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_l;/* '<Root>/VENT_GND_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_b;/* '<Root>/PACE_GND_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_j;/* '<Root>/PACE_CHARGE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_h;/* '<Root>/ATR_PACE_CTRL' */
  freedomk64f_DigitalWrite_Grou_T obj_h5;/* '<Root>/ATR_GND_CTRL' */
  freedomk64f_PWMOutput_Group44_T obj_g;/* '<Root>/VENT_CMP_REF_PWM' */
  freedomk64f_PWMOutput_Group44_T obj_lh;/* '<Root>/PACING_REF_PWM' */
  uint32_T temporalCounter_i1;         /* '<S1>/Chart' */
  uint8_T is_c3_Group44VVI;            /* '<S1>/Chart' */
  uint8_T is_active_c3_Group44VVI;     /* '<S1>/Chart' */
} DW_Group44VVI_T;

/* Parameters (default storage) */
struct P_Group44VVI_T_ {
  real_T VENT_CMP_DETECT_SampleTime;   /* Expression: SampleTime
                                        * Referenced by: '<Root>/VENT_CMP_DETECT'
                                        */
  real_T p_lowrateInterval_Value;      /* Expression: 1000
                                        * Referenced by: '<Root>/p_lowrateInterval'
                                        */
  real_T p_vSensitivity_Value;         /* Expression: 3
                                        * Referenced by: '<Root>/p_vSensitivity'
                                        */
  real_T p_vPaceWidth_Value;           /* Expression: 4
                                        * Referenced by: '<Root>/p_vPaceWidth'
                                        */
  real_T p_vPaceAmp_Value;             /* Expression: 4
                                        * Referenced by: '<Root>/p_vPaceAmp'
                                        */
  real_T p_VRP_Value;                  /* Expression: 200
                                        * Referenced by: '<Root>/p_VRP'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_Group44VVI_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_Group44VVI_T Group44VVI_P;

/* Block signals (default storage) */
extern B_Group44VVI_T Group44VVI_B;

/* Block states (default storage) */
extern DW_Group44VVI_T Group44VVI_DW;

/* Model entry point functions */
extern void Group44VVI_initialize(void);
extern void Group44VVI_step(void);
extern void Group44VVI_terminate(void);

/* Real-time Model object */
extern RT_MODEL_Group44VVI_T *const Group44VVI_M;
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
 * '<Root>' : 'Group44VVI'
 * '<S1>'   : 'Group44VVI/Subsystem'
 * '<S2>'   : 'Group44VVI/Subsystem/Chart'
 */
#endif                                 /* RTW_HEADER_Group44VVI_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
