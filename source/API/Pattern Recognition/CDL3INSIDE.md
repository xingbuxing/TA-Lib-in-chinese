# CDL3INSIDE

   /* Proceed with the calculation for the requested range.
    * Must have:
    * - first candle: long white (black) real body
    * - second candle: short real body totally engulfed by the first
    * - third candle: black (white) candle that closes lower (higher) than the first candle's open
    * The meaning of "short" and "long" is specified with TA_SetCandleSettings
    * outInteger is positive (1 to 100) for the three inside up or negative (-1 to -100) for the three inside down; 
    * the user should consider that a three inside up is significant when it appears in a downtrend and a three inside
    * down is significant when it appears in an uptrend, while this function does not consider the trend
    */
   outIdx = 0;
   do
   {
#ifdef TA_LIB_PRO
      /* Section for code distributed with TA-Lib Pro only. */
#else
        if( TA_REALBODY(i-2) > TA_CANDLEAVERAGE( BodyLong, BodyLongPeriodTotal, i-2 ) &&         // 1st: long
            TA_REALBODY(i-1) <= TA_CANDLEAVERAGE( BodyShort, BodyShortPeriodTotal, i-1 ) &&      // 2nd: short
            max( inClose[i-1], inOpen[i-1] ) < max( inClose[i-2], inOpen[i-2] ) &&                  //      engulfed by 1st
            min( inClose[i-1], inOpen[i-1] ) > min( inClose[i-2], inOpen[i-2] ) &&
            ( ( TA_CANDLECOLOR(i-2) == 1 && TA_CANDLECOLOR(i) == -1 && inClose[i] < inOpen[i-2] )   // 3rd: opposite to 1st
              ||                                                                                    //      and closing out
              ( TA_CANDLECOLOR(i-2) == -1 && TA_CANDLECOLOR(i) == 1 && inClose[i] > inOpen[i-2] )
            )
          )
#endif
            outInteger[outIdx++] = -TA_CANDLECOLOR(i-2) * 100;
            
            

three inside down，在上升趋势中，空头信号
第一根K线，长阳线
第二根k线，实体完全包含于第一根K线的实体，并且实体较短
第三根K线，阴线，并且收盘价低于第1根K线的开盘价

three inside up，在下降趋势，多头信号
第一根K线，长阴线
第二根k线，实体完全包含于第一根K线的实体，并且实体较短
第三根K线，阳线，并且收盘价大于第1根K线的开盘价

