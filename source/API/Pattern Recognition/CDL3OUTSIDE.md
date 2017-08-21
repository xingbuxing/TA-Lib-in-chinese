# CDL3OUTSIDE

three outside up，在下降趋势，多头信号
第一根K线，阴线
第二根k线，阳线，实体完全包含第一根K线的实体
第三根K线，收盘价比前一根K线要高


three outside outside，在上升趋势中，空头信号
第一根K线，阳线
第二根k线，阴线，实体完全包含第一根K线的实体
第三根K线，收盘价比前一根K线要低


   /* Proceed with the calculation for the requested range.
    * Must have:
    * - first: black (white) real body
    * - second: white (black) real body that engulfs the prior real body
    * - third: candle that closes higher (lower) than the second candle
    * outInteger is positive (1 to 100) for the three outside up or negative (-1 to -100) for the three outside down;
    * the user should consider that a three outside up must appear in a downtrend and three outside down must appear
    * in an uptrend, while this function does not consider it
    */
   outIdx = 0;
   do
   {
        if( ( TA_CANDLECOLOR(i-1) == 1 && TA_CANDLECOLOR(i-2) == -1 &&          // white engulfs black
              inClose[i-1] > inOpen[i-2] && inOpen[i-1] < inClose[i-2] &&
              inClose[i] > inClose[i-1]                                         // third candle higher
            )
            ||
            ( TA_CANDLECOLOR(i-1) == -1 && TA_CANDLECOLOR(i-2) == 1 &&          // black engulfs white
              inOpen[i-1] > inClose[i-2] && inClose[i-1] < inOpen[i-2] &&
              inClose[i] < inClose[i-1]                                         // third candle lower
            )
          )
       {
#ifdef TA_LIB_PRO
      /* Section for code distributed with TA-Lib Pro only. */
#else
            outInteger[outIdx++] = TA_CANDLECOLOR(i-1) * 100;
#endif
