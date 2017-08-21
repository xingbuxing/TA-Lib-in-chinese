# CDL3BLACKCROWS

* - three consecutive and declining black candlesticks
* - each candle must have no or very short lower shadow
* - each candle after the first must open within the prior candle's real body
* - the first candle's close should be under the prior white candle's high

* The meaning of "very short" is specified with TA_SetCandleSettings
* outInteger is negative (-1 to -100): three black crows is always bearish; 
* the user should consider that 3 black crows is significant when it appears after a mature advance or at high levels, 
* while this function does not consider it

      /* Section for code distributed with TA-Lib Pro only. */
#else
        if( TA_CANDLECOLOR(i-3) == 1 &&                                         // white
            TA_CANDLECOLOR(i-2) == -1 &&                                        // 1st black
            TA_LOWERSHADOW(i-2) < TA_CANDLEAVERAGE( ShadowVeryShort, ShadowVeryShortPeriodTotal[2], i-2 ) &&     
                                                                                // very short lower shadow
            TA_CANDLECOLOR(i-1) == -1 &&                                        // 2nd black
            TA_LOWERSHADOW(i-1) < TA_CANDLEAVERAGE( ShadowVeryShort, ShadowVeryShortPeriodTotal[1], i-1 ) &&     
                                                                                // very short lower shadow
            TA_CANDLECOLOR(i) == -1 &&                                          // 3rd black
            TA_LOWERSHADOW(i) < TA_CANDLEAVERAGE( ShadowVeryShort, ShadowVeryShortPeriodTotal[0], i ) &&         
                                                                                // very short lower shadow
            inOpen[i-1] < inOpen[i-2] && inOpen[i-1] > inClose[i-2] &&          // 2nd black opens within 1st black's rb
            inOpen[i] < inOpen[i-1] && inOpen[i] > inClose[i-1] &&              // 3rd black opens within 2nd black's rb
            inHigh[i-3] > inClose[i-2] &&                                       // 1st black closes under prior candle's high
            inClose[i-2] > inClose[i-1] &&                                      // three declining
            inClose[i-1] > inClose[i]                                           // three declining
          )
#endif
            outInteger[outIdx++] = -100;



由4根k线组成。
第一根K线是阳线。后面三根都是阴线。后面3根k线的收盘价，逐渐降低。
每根阴线的下影线都非常的短。或者没有。
第三、第四根K线的开盘价，都得在前一根K线的实体当中。
第二根K线的收盘价，必须比第一根阳线的最高价低

