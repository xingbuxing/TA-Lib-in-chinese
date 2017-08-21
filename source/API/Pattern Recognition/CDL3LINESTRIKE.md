# CDL3LINESTRIKE


连续三个阳线，收盘价逐渐提高。

每跟线的开盘价，都在前几根线实体的中间。或者接近。

第四根线：阴线，开盘价比前一根线的收盘价高，但是收盘价比第一根k线的开盘价低。
上涨信号，返回100




连续三个阴线，收盘价逐渐降低。

每跟线的开盘价，都在前几根线实体的中间。或者接近。

第四根线：阳线，开盘价比前一根线的收盘价低，但是收盘价比第一根k线的开盘价高。

下跌信号，返回-100

   /* Proceed with the calculation for the requested range.
    * Must have:
    * - three white soldiers (three black crows): three white (black) candlesticks with consecutively higher (lower) closes,
    * each opening within or near the previous real body
    * - fourth candle: black (white) candle that opens above (below) prior candle's close and closes below (above) 
    * the first candle's open
    * The meaning of "near" is specified with TA_SetCandleSettings;
    * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
    * the user should consider that 3-line strike is significant when it appears in a trend in the same direction of
    * the first three candles, while this function does not consider it
    */
   outIdx = 0;
   do
   {
#ifdef TA_LIB_PRO
      /* Section for code distributed with TA-Lib Pro only. */
#else
        if( TA_CANDLECOLOR(i-3) == TA_CANDLECOLOR(i-2) &&                                   // three with same color
            TA_CANDLECOLOR(i-2) == TA_CANDLECOLOR(i-1) &&
            TA_CANDLECOLOR(i) == -TA_CANDLECOLOR(i-1) &&                                    // 4th opposite color
                                                                                            // 2nd opens within/near 1st rb
            inOpen[i-2] >= min( inOpen[i-3], inClose[i-3] ) - TA_CANDLEAVERAGE( Near, NearPeriodTotal[3], i-3 ) &&
            inOpen[i-2] <= max( inOpen[i-3], inClose[i-3] ) + TA_CANDLEAVERAGE( Near, NearPeriodTotal[3], i-3 ) &&
                                                                                            // 3rd opens within/near 2nd rb
            inOpen[i-1] >= min( inOpen[i-2], inClose[i-2] ) - TA_CANDLEAVERAGE( Near, NearPeriodTotal[2], i-2 ) &&
            inOpen[i-1] <= max( inOpen[i-2], inClose[i-2] ) + TA_CANDLEAVERAGE( Near, NearPeriodTotal[2], i-2 ) &&
            (
                (   // if three white
                    TA_CANDLECOLOR(i-1) == 1 &&
                    inClose[i-1] > inClose[i-2] && inClose[i-2] > inClose[i-3] &&           // consecutive higher closes
                    inOpen[i] > inClose[i-1] &&                                             // 4th opens above prior close
                    inClose[i] < inOpen[i-3]                                                // 4th closes below 1st open
                ) ||
                (   // if three black
                    TA_CANDLECOLOR(i-1) == -1 &&
                    inClose[i-1] < inClose[i-2] && inClose[i-2] < inClose[i-3] &&           // consecutive lower closes
                    inOpen[i] < inClose[i-1] &&                                             // 4th opens below prior close
                    inClose[i] > inOpen[i-3]                                                // 4th closes above 1st open
                )
            )
          )
            outInteger[outIdx++] = TA_CANDLECOLOR(i-1) * 100;
        else
            outInteger[outIdx++] = 0;
            


