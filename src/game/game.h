#pragma once

#include "global/types.h"

#include <stdbool.h>
#include <stdint.h>

bool Game_Start(int32_t level_num, GAMEFLOW_LEVEL_TYPE level_type);
int32_t StopGame(void);
int32_t GameLoop(GAMEFLOW_LEVEL_TYPE level_type);
