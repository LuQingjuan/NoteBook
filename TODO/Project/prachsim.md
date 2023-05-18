#### dlschsim
##### 编译
```
source oaienv 
cd openairinterface5g/cmake_targets/
./build_oai --phy_simulators
```

##### CI
```
cd cmake_targets/autotests
./run_exec_autotests.bash -c test_case_list.xml

cat cmake_targets/autotests/log/results_autotests.xml
```

##### 手动运行
```
cd cmake_targets/ran_build/build/
./nr_prachsim -a -s -30 -n 100 -p 63 -R 106
./nr_prachsim -a -s -30 -n 100 -p 63 -R 217
./nr_prachsim -a -s -30 -n 100 -p 63 -R 273
./nr_prachsim -a -s -30 -n 100 -p 63 -R 106 -c 4
./nr_prachsim -a -s -30 -n 100 -p 32 -R 32 -m 3 -c52
./nr_prachsim -a -s -30 -n 100 -p 32 -R 66 -m 3 -c52
./nr_prachsim -a -s -30 -n 100 -R 66 -m 3 -c52 -H
./nr_prachsim -a -s -30 -n 100 -p 99 -R 25 -m 0
```

##### 参数说明
`./nr_prachsim -h(elp) -a(wgn on) -p(extended_prefix) -N cell_id -f output_filename -F input_filename -g channel_model -n n_frames -s snr0 -S snr1 -x transmission_mode -y TXant -z RXant -i Intefrence0 -j Interference1 -A interpolation_file -C(alibration offset dB) -N CellId`
| 参数 | \                                                                                                                                                          | 说明                                                                                                                                                           |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -h   | -h此消息                                                                                                                                                   | This message                                                                                                                                                   |
| -a   | -a使用AWGN信道，而不是多路径                                                                                                                               | Use AWGN channel and not multipath                                                                                                                             |
| -n   | -n要模拟的帧数                                                                                                                                             | Number of frames to simulate                                                                                                                                   |
| -s   | -s起始SNR，从SNR0运行到SNR0+5dB。如果n_frames为1，则仅模拟SNR                                                                                              | Starting SNR, runs from SNR0 to SNR0 + 5 dB.  If n_frames is 1 then just SNR is simulated                                                                      |
| -S   | -S结束SNR，从SNR0运行到SNR1                                                                                                                                | Ending SNR, runs from SNR0 to SNR1                                                                                                                             |
| -g   | -g[A，B，C，D，E，F，g，I，N]使用3GPP SCM（A，B，C，D）或36-101（E-EPA，F-EVA，g-ETU）或Rayleigh1（I）或Rayleigh1_800（N）模型（忽略延迟扩展和Ricean因子） | [A,B,C,D,E,F,G,I,N] Use 3GPP SCM (A,B,C,D) or 36-101 (E-EPA,F-EVA,G-ETU) or Rayleigh1 (I) or Rayleigh1_800 (N) models (ignores delay spread and Ricean factor) |
| -z   | -z gNB中使用的RX天线数量                                                                                                                                   | Number of RX antennas used in gNB                                                                                                                              |
| -N   | -N镍氢电池                                                                                                                                                 | Nid_cell                                                                                                                                                       |
| -O   | -O过采样因子（1,2,4,8,16）                                                                                                                                 | oversampling factor (1,2,4,8,16)                                                                                                                               |
| -d   | -d信道延迟                                                                                                                                                 | Channel delay                                                                                                                                                  |
| -v   | -v起始UE速度（km/h），从“v”到“v+50km/h”。如果n_frames为1，则仅模拟“v”                                                                                      | Starting UE velocity in km/h, runs from 'v' to 'v+50km/h'. If n_frames is 1 just 'v' is simulated                                                              |
| -V   | -V终端UE速度（km/h），从“V”到“V”-L rootSequenceIndex（0-837）                                                                                              | Ending UE velocity in km/h, runs from 'v' to 'V'-L rootSequenceIndex (0-837)                                                                                   |
| -Z   | -Z NCS_config（零相关区）（0-15）                                                                                                                          | NCS_config (ZeroCorrelationZone) (0-15)                                                                                                                        |
| -H   | -启用高速标志的H Run                                                                                                                                       | Run with High-Speed Flag enabled                                                                                                                               |
| -R   | -R PRB数量（6,15,25,50,75100）                                                                                                                             | Number of PRB (6,15,25,50,75,100)                                                                                                                              |
| -F   | -F RX一致性测试的输入文件名（.txt格式）                                                                                                                    | Input filename (.txt format) for RX conformance testing                                                                                                        |
jftt@jftt-pc:~/work_jftt/lu/mtc-oai/cmake_targets/ran_build/build$ 

##### 代码解析
* prachsim
```mermaid
    sequenceDiagram
Note right of main :            int main(int argc, char **argv)
Note right of main :            cpuf = get_cpu_freq_GHz()
                                alt if ( load_configmodule(argc,argv,CONFIG_ENABLECMDLINEONLY) == 0)
                                end
Note right of main :            exit_fun("[SOFTMODEM] Error, configuration module init failed\n")
Note right of main :            randominit(0)
                                loop while ((c = getopt (argc, argv, "hHaA:Cc:l:r:p:g:m:n:s:S:t:x:y:v:V:z:N:F:d:Z:L:R:E")) != -1)
                                end
Note right of main :            switch (c)
Note right of main :            switch((char)*optarg)
Note right of main :            exit(-1)
                                alt if ((NCS_config > 15) || (NCS_config < 0))
                                end
                                alt if ((rootSequenceIndex < 0) || (rootSequenceIndex > 837))
                                end
                                alt if ((transmission_mode!=1) &&
                                end
Note right of main :            exit(-1)
                                alt if ((n_tx==0) || (n_tx>2))
                                end
Note right of main :            exit(-1)
                                alt if ((n_rx==0) || (n_rx>2))
                                end
Note right of main :            exit(-1)
Note right of main :            input_fd = fopen(optarg,"r")
                                alt if (input_fd==NULL)
                                end
Note right of main :            exit(-1)
Note right of main :            exit (-1)
Note right of main :            logInit()
Note right of main :            set_glog(loglvl)
Note right of main :            SET_LOG_DEBUG(PRACH)
Note right of main :            nr_phy_config_request_sim(gNB, N_RB_UL, N_RB_UL, mu, Nid_cell, SSB_positions)
Note right of main :            uint64_t absoluteFrequencyPointA = to_nrarfcn(frame_parms->nr_band,
                                alt if (config_index<67 && mu != 3)  { prach_sequence_length=0; slot = subframe * frame_parms->slots_per_subframe; }
                                end
                                alt if (mu == 0)
                                else if (mu == 1)
                                else if (mu == 3)
                                end
Note right of main :            exit(-1)
Note right of main :            int ret = get_nr_prach_info_from_index(config_index,
                                alt if (ret == 0) {printf("No prach in %d.%d, mu %d, config_index %d\n",frame,slot,mu,config_index); exit(-1);}
                                end
                                alt if (format1 != 0xff)
                                end
Note right of main :            switch(format0)
Note right of main :            switch(format0) { // single PRACH format
Note right of main :            prach_pdu->num_cs                                                                      = get_NCS(NCS_config, format0, restrictedSetConfig)
Note right of main :            set_tdd_config_nr(&gNB->gNB_config, mu, 7, 6, 2, 4)
Note right of main :            phy_init_nr_gNB(gNB)
Note right of main :            nr_phy_init_RU(ru)
                                alt if (init_nr_ue_signal(UE, 1) != 0)
                                end
Note right of main :            exit(-1)
Note right of main :            ue_prach_pdu->num_cs          = get_NCS(NCS_config, format0, restrictedSetConfig)
                                alt if (preamble_tx == 99)
                                end
Note right of main :            preamble_tx = (uint16_t)(taus()&0x3f)
                                alt if (n_frames == 1)
                                end
Note right of main :            UE2gNB = new_channel_desc_scm(UE->frame_parms.nb_antennas_tx,
                                alt if (UE2gNB==NULL)
                                end
Note right of main :            exit(-1)
Note right of main :            i=0
                                loop i<2
Note right of main :
Note right of main :            i++
                                end
                            )
Note right of main :            compute_nr_prach_seq(prach_config->prach_sequence_length.value,
Note right of main :            compute_nr_prach_seq(ue_prach_config->prach_sequence_length,
Note right of main :            generate_nr_prach(UE, 0, frame, slot)
Note right of main :            i = 0
                                loop i < frame_parms->samples_per_subframe
Note right of main :
Note right of main :            i++
                                end
                            )
Note right of main :            aa=0
                                loop aa<1
Note right of main :
Note right of main :            aa++
                                end
                            )
                                alt if (awgn_flag == 0)
                                end
Note right of main :            aarx=0
                                loop aarx<gNB->frame_parms.nb_antennas_rx
Note right of main :
Note right of main :            aarx++
                                end
                            )
                                alt if (aa==0)
                                end
                                alt if (snr1set == 0)
                                end
                                alt if (n_frames == 1)
                                end
                                alt if (ue_speed1set == 0)
                                end
                                alt if (n_frames == 1)
                                end
                                alt if (n_frames==1) printf("slot %d, rx_prach_start %d\n",slot,rx_prach_start)
                                end
Note right of main :            SNR=snr0
                                loop SNR<snr1
Note right of main :
Note right of main :            SNR+=.1
                                end
                            )
Note right of main :            ue_speed=ue_speed0
                                loop ue_speed<ue_speed1
Note right of main :
Note right of main :            ue_speed+=10
                                end
                            )
Note right of main :            trial=0
                                loop trial<n_frames
Note right of main :
Note right of main :            trial++
                                end
                            )
                                alt if (input_fd==NULL)
                                end
Note right of main :            sigma2_dB = 10*log10((double)tx_lev) - SNR - 10*log10(N_RB_UL*12/N_ZC)
                                alt if (n_frames==1)
                                end
Note right of main :            sigma2 = pow(10,sigma2_dB/10)
                                alt if (awgn_flag == 0)
                                end
Note right of main :            multipath_tv_channel(UE2gNB, s_re, s_im, r_re, r_im, frame_parms->samples_per_frame, 0)
                                alt if (n_frames==1)
                                end
Note right of main :            10*log10(signal_energy_fp(r_re,r_im,1,OFDM_SYMBOL_SIZE_COMPLEX_SAMPLES,0)),
Note right of main :            10*log10(tx_lev))
Note right of main :            i = 0
                                loop i< frame_parms->samples_per_subframe
Note right of main :
Note right of main :            i++
                                end
                            )
Note right of main :            aa = 0
                                loop aa < frame_parms->nb_antennas_rx
Note right of main :
Note right of main :            aa++
                                end
                            )
Note right of main :            ((short*) &ru->common.rxdata[aa][rx_prach_start])[2*i] = (short) (.167*(r_re[aa][i] +sqrt(sigma2/2)*gaussdouble(0.0,1.0)))
Note right of main :            ((short*) &ru->common.rxdata[aa][rx_prach_start])[2*i+1] = (short) (.167*(r_im[aa][i] + (iqim*r_re[aa][i]) + sqrt(sigma2/2)*gaussdouble(0.0,1.0)))
Note right of main :            n_bytes = fread(&ru->common.rxdata[0][rx_prach_start],sizeof(int32_t),frame_parms->samples_per_subframe,input_fd)
                                alt if (n_bytes!=frame_parms->samples_per_subframe)
                                end
Note right of main :            exit(-1)
Note right of main :            l = 0
                                loop l < frame_parms->symbols_per_slot
Note right of main :
Note right of main :            l++
                                end
                            )
Note right of main :            aa = 0
                                loop aa < frame_parms->nb_antennas_rx
Note right of main :
Note right of main :            aa++
                                end
                            )
Note right of main :            nr_slot_fep_ul(frame_parms,
Note right of main :            rx_nr_prach_ru(ru, prach_format, numRA, prachStartSymbol, prachOccasion, frame, slot)
Note right of main :            int i = 0
                                loop i < ru->nb_rx
Note right of main :
Note right of main :            ++i
                                end
                            )
                                alt if (n_frames == 1) printf("ncs %d,num_seq %d\n",prach_pdu->num_cs,  prach_config->num_prach_fd_occasions_list[fd_occasion].num_root_sequences.value)
                                end
Note right of main :            rx_nr_prach(gNB, prach_pdu, prachOccasion, frame, subframe, &preamble_rx, &preamble_energy, &preamble_delay)
                                alt if (preamble_rx != preamble_tx)
                                end
                                alt if (n_frames==1)
                                end
                                alt if (input_fd)
                                end
                                alt if (prach_errors)
                                end
                                alt if (!prach_errors)
                                end
                                alt if (input_fd)
                                end
Note right of main :            free_channel_desc_scm(UE2gNB)
Note right of main :            nr_phy_free_RU(ru)
Note right of main :            phy_free_nr_gNB(gNB)
Note right of main :            int i = 0
                                loop i < nb_slots_to_set
Note right of main :
Note right of main :            ++i
                                end
                            )
Note right of main :            term_nr_ue_signal(UE, 1)
Note right of main :            i=0
                                loop i<2
Note right of main :
Note right of main :            i++
                                end
                            )
                                alt if (input_fd) fclose(input_fd)
                                end
Note right of main :            loader_reset()
Note right of main :            logTerm()
Note right of main :            return(0)
```
