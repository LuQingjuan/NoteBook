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
./nr_dlsim -n100 -R106 -b106 -s5
./nr_dlsim -n100 -R217 -b217 -s5
./nr_dlsim -n100 -R273 -b273 -s5
./nr_dlsim -n100 -s1 -S2 -t25
./nr_dlsim -n100 -s1 -S2 -t33
./nr_dlsim -n100 -s5 -S7 -t50
./nr_dlsim -n100 -m0 -e0 -R25 -b25 -i 2 1 0
./nr_dlsim -n100 -R106 -a25 -s5
./nr_dlsim -n100 -R106 -a51 -s5
./nr_dlsim -n100 -R217 -b100 -s5
./nr_dlsim -n100 -R217 -a80 -s5
./nr_dlsim -n100 -R217 -a110 -s5 -b100
./nr_dlsim -n100 -e27 -s30
./nr_dlsim -n100 -e16 -s11 -S13
./nr_dlsim -n100 -q1 -e26 -s30
./nr_dlsim -n100 -e0 -t95 -S-1.0 -i 2 1 0
./nr_dlsim -n10 -s20 -U 3 0 0 2 -gR -x1 -y4 -z4
./nr_dlsim -n10 -s20 -U 3 0 0 2 -gR -x2 -y4 -z4
./nr_dlsim -n10 -s20 -U 3 0 0 2 -x4 -y4 -z4
./nr_dlsim -n100 -s5 -T 2 2 2
./nr_dlsim -n100 -s5 -T 2 1 2
./nr_dlsim -n100 -s5 -T 2 0 4
./nr_dlsim -n100 -s5 -S7 -U 2 0 1
./nr_dlsim -n100 -s5 -S7 -U 2 0 2
./nr_dlsim -n100 -s5 -S7 -U 2 1 3
```

##### 参数说明
`./nr_dlsim -h(elp) -p(extended_prefix) -N cell_id -f output_filename -F input_filename -g channel_model -n n_frames -s snr0 -S snr1 -x transmission_mode -y TXant -z RXant -i Intefrence0 -j Interference1 -A interpolation_file -C(alibration offset dB) -N CellId`
| 参数 |                                                                                                                                    | 说明                                                                                                                                                                                            |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -h   | -h此消息                                                                                                                           | This message                                                                                                                                                                                    |
| -L   | -L<日志级别，0（错误），1（警告），2（分析），3（信息），4（调试），5（跟踪）>                                                     | <log level, 0(errors), 1(warning), 2(analysis), 3(info), 4(debug), 5(trace)>                                                                                                                    |
| -n   | -n要模拟的帧数                                                                                                                     | Number of frames to simulate                                                                                                                                                                    |
| -s   | -s起始SNR，从SNR0运行到SNR0+5dB。如果n_frames为1，则仅模拟SNR                                                                      | Starting SNR, runs from SNR0 to SNR0 + 5 dB.  If n_frames is 1 then just SNR is simulated                                                                                                       |
| -S   | -S结束SNR，从SNR0运行到SNR1                                                                                                        | Ending SNR, runs from SNR0 to SNR1                                                                                                                                                              |
| -g   | -g[A，B，C，D，E，F，g，R]使用3GPP SCM（A、B、C、D）或36-101（E-EPA、F-EVA、g-ETU）模型或R用于MIMO模型（忽略延迟扩展和Ricean因子） | [A,B,C,D,E,F,G,R] Use 3GPP SCM (A,B,C,D) or 36-101 (E-EPA,F-EVA,G-ETU) models or R for MIMO model (ignores delay spread and Ricean factor)                                                      |
| -y   | -y gNB中使用的TX天线数量                                                                                                           | Number of TX antennas used in gNB                                                                                                                                                               |
| -z   | -z UE中使用的RX天线数量                                                                                                            | Number of RX antennas used in UE                                                                                                                                                                |
| -x   | -x PDSCH的层数                                                                                                                     | Num of layer for PDSCH                                                                                                                                                                          |
| -p   | -p预编码矩阵索引                                                                                                                   | Precoding matrix index                                                                                                                                                                          |
| -i   | -i改变信道估计技术。参数列表：频域｛0:线性插值，1:基于PRB的平均｝，时域｛0:最后一个DMRS符号的估计，1:DMRS符号平均｝                | Change channel estimation technique. Arguments list: Frequency domain {0:Linear interpolation, 1:PRB based averaging}, Time domain {0:Estimates of last DMRS symbol, 1:Average of DMRS symbols} |
| -R   | -R N_RB_DL                                                                                                                         | N_RB_DL                                                                                                                                                                                         |
| -O   | -O过采样因子（1,2,4,8,16）                                                                                                         | oversampling factor (1,2,4,8,16)                                                                                                                                                                |
| -A   | -Interpolation_filname使用抽象运行，使用文件中的插值多项式生成散点图                                                               | Interpolation_filname Run with Abstraction to generate Scatter plot using interpolation polynomial in file                                                                                      |
| -f   | -f包含RRC配置的原始文件（由gNB生成）                                                                                               | raw file containing RRC configuration (generated by gNB)                                                                                                                                        |
| -F   | -F RX一致性测试的输入文件名（.txt格式）                                                                                            | Input filename (.txt format) for RX conformance testing                                                                                                                                         |
| -o   | -o CORESET偏移                                                                                                                     | CORESET offset                                                                                                                                                                                  |
| -a   | -PDSCH的启动PRB                                                                                                                    | Start PRB for PDSCH                                                                                                                                                                             |
| -b   | -b PDSCH的PRB数量                                                                                                                  | Number of PRB for PDSCH                                                                                                                                                                         |
| -c   | -c PDSCH的起始符号                                                                                                                 | Start symbol for PDSCH (fixed for now)                                                                                                                                                          |
| -j   | -j PDSCH的符号数量                                                                                                                 | Number of symbols for PDSCH (fixed for now)                                                                                                                                                     |
| -e   | -e MSC索引                                                                                                                         | MSC index                                                                                                                                                                                       |
| -q   | -q MCS表索引                                                                                                                       | MCS Table index                                                                                                                                                                                 |
| -t   | -t可接受的有效吞吐量（百分比）                                                                                                     | Acceptable effective throughput (in percentage)                                                                                                                                                 |
| -I   | -I LDPC解码器最大迭代次数                                                                                                          | Maximum LDPC decoder iterations                                                                                                                                                                 |
| -T   | -T启用PTRS，参数列表L_PTRS｛0，1，2｝K_PTRS{2，4｝，例如-T 2 0 2                                                                   | Enable PTRS, arguments list L_PTRS{0,1,2} K_PTRS{2,4}, e.g. -T 2 0 2                                                                                                                            |
| -U   | -U更改DMRS配置，参数列表DMRS类型｛0=A，1=B｝DMRS AddPos｛0:2｝DMRSConfType｛1:2｝，例如-U 3 0 2 1                                  | Change DMRS Config, arguments list DMRS TYPE{0=A,1=B} DMRS AddPos{0:2} DMRS ConfType{1:2}, e.g. -U 3 0 2 1                                                                                      |
| -P   | -P打印DLSCH性能                                                                                                                    | Print DLSCH performances                                                                                                                                                                        |
| -v   | -v最大轮次                                                                                                                         | Maximum number of rounds                                                                                                                                                                        |
| -w   | -w将txdata写入二进制文件（一帧）                                                                                                   | Write txdata to binary file (one frame)                                                                                                                                                         |
| -d   | -d dlsch线程数，0：无dlsch并行化                                                                                                   | number of dlsch threads, 0: no dlsch parallelization                                                                                                                                            |
| -X   | -X gNB线程池配置，n=>无线程                                                                                                        | gNB thread pool configuration, n => no threads                                                                                                                                                  |
| -Y   | -Y在UE中运行初始同步                                                                                                               | Run initial sync in UE                                                                                                                                                                          |

##### 代码解析
* dlsim
```mermaid
    sequenceDiagram
Note right of main :            int main(int argc, char **argv)
Note right of main :            setbuf(stdout, NULL)
Note right of main :            cpuf = get_cpu_freq_GHz()
                                alt if ( load_configmodule(argc,argv,CONFIG_ENABLECMDLINEONLY) == 0)
                                end
Note right of main :            exit_fun("[NR_DLSIM] Error, configuration module init failed\n")
Note right of main :            randominit(0)
                                loop while ((c = getopt(argc, argv, "f:hA:p:f:g:i:n:s:S:t:v:x:y:z:M:N:F:GR:d:PI:L:a:b:e:m:w:T:U:q:X:Y")) != -1)
                                end
Note right of main :            switch (c)
Note right of main :            scg_fd = fopen(optarg,"r")
                                alt if (scg_fd==NULL)
                                end
Note right of main :            exit(-1)
Note right of main :            switch((char)*optarg)
Note right of main :            exit(-1)
Note right of main :            i=0
                                loop i < atoi(optarg)
Note right of main :
Note right of main :            i++
                                end
                            )
                                alt if ((g_nrOfLayers == 0) || (g_nrOfLayers > 4))
                                end
Note right of main :            exit(-1)
                                alt if ((n_tx==0) || (n_tx>4)) {//extend gNB to support n_tx = 4
                                end
Note right of main :            exit(-1)
                                alt if ((n_rx==0) || (n_rx>4)) {//extend UE to support n_tx = 4
                                end
Note right of main :            exit(-1)
Note right of main :            input_fd = fopen(optarg,"r")
                                alt if (input_fd==NULL)
                                end
Note right of main :            exit(-1)
Note right of main :            eff_tp_check = (float)atoi(optarg)/100
Note right of main :            output_fd = fopen("txdata.dat", "w+")
Note right of main :            i=0
                                loop i < atoi(optarg)
Note right of main :
Note right of main :            i++
                                end
                            )
Note right of main :            i=0
                                loop i < atoi(optarg)
Note right of main :
Note right of main :            i++
                                end
                            )
Note right of main :            gNBthreads[sizeof(gNBthreads)-1]=0
Note right of main :            exit (-1)
Note right of main :            logInit()
Note right of main :            set_glog(loglvl)
Note right of main :            InitSinLUT()
Note right of main :            get_softmodem_params()->phy_test = 1
Note right of main :            get_softmodem_params()->do_ra = 0
Note right of main :            set_softmodem_optmask(SOFTMODEM_DLSIM_BIT)
                                alt if (snr1set==0)
                                end
Note right of main :            i = 0
                                loop i < RC.nb_nr_macrlc_inst
Note right of main :
Note right of main :            i++
                                end
                            )
Note right of main :            mac_top_init_gNB(ngran_gNB)
Note right of main :            int msg_len=fread(buffer,1,1024,scg_fd)
Note right of main :            asn_dec_rval_t dec_rval = uper_decode_complete( NULL,
                                alt if ((dec_rval.code != RC_OK) && (dec_rval.consumed == 0))
                                end
Note right of main :            exit(-1)
Note right of main :            fclose(scg_fd)
Note right of main :            dec_rval = uper_decode_complete( NULL,
                                alt if ((dec_rval.code != RC_OK) && (dec_rval.consumed == 0))
                                end
Note right of main :            exit(-1)
Note right of main :            prepare_scc(scc)
Note right of main :            fill_scc_sim(scc, &ssb_bitmap, N_RB_DL, N_RB_DL, mu, mu)
Note right of main :            fix_scc(scc, ssb_bitmap)
Note right of main :            prepare_scd(scd)
Note right of main :            validate_input_pmi(pdsch_AntennaPorts, g_nrOfLayers, g_pmi)
Note right of main :            prepare_sim_uecap(UE_Capability_nr,scc,mu,
Note right of main :            NR_CellGroupConfig_t *secondaryCellGroup = get_default_secondaryCellGroup(scc, scd, UE_Capability_nr, 0, 1, &conf, 0)
Note right of main :            fix_scd(scd)
                                alt if(modify_dmrs)
                                end
Note right of main :            update_dmrs_config(secondaryCellGroup, dmrs_arg)
                                alt if(enable_ptrs)
                                end
Note right of main :            update_ptrs_config(secondaryCellGroup, &rbSize, &mcsIndex, ptrs_arg)
Note right of main :            nr_mac_config_scc(RC.nrmac[0], pdsch_AntennaPorts, n_tx, 0, 6, scc)
Note right of main :            nr_mac_add_test_ue(RC.nrmac[0], secondaryCellGroup->spCellConfig->reconfigurationWithSync->newUE_Identity, secondaryCellGroup)
Note right of main :            phy_init_nr_gNB(gNB)
Note right of main :            configure_UE_BWP(RC.nrmac[0], scc, &UE_info->UE_sched_ctrl, NULL, UE_info, -1, -1)
                                alt if (g_mcsIndex < 0) g_mcsIndex = 9
                                end
                                alt if (g_rbStart < 0) g_rbStart=0
                                end
                                alt if (g_rbSize < 0) g_rbSize = N_RB_DL - g_rbStart
                                end
Note right of main :            get_samplerate_and_bw(mu,
Note right of main :            gNB2UE = new_channel_desc_scm(n_tx,
                                alt if (gNB2UE==NULL)
                                end
Note right of main :            exit(-1)
Note right of main :            i=0
                                loop i<n_tx
Note right of main :
Note right of main :            i++
                                end
                            )
Note right of main :            i=0
                                loop i<n_rx
Note right of main :
Note right of main :            i++
                                end
                            )
                                alt if (pbch_file_fd!=NULL)
                                end
Note right of main :            load_pbch_desc(pbch_file_fd)
                                alt if (run_initial_sync==1)
                                end
                                alt if (init_nr_ue_signal(UE, 1) != 0)
                                end
Note right of main :            exit(-1)
Note right of main :            init_nr_ue_transport(UE)
Note right of main :            nr_gold_pbch(UE)
Note right of main :            nr_gold_pdcch(UE, frame_parms->Nid_cell)
Note right of main :            int i = 0
                                loop i < 2
Note right of main :
Note right of main :            i++
                                end
                            )
Note right of main :            nr_gold_pdsch(UE, i, UE->scramblingID_dlsch[i])
Note right of main :            nr_l2_init_ue(NULL)
Note right of main :            UE_mac = get_mac_inst(0)
Note right of main :            ue_init_config_request(UE_mac, mu)
Note right of main :            UE->if_inst = nr_ue_if_module_init(0)
Note right of main :            UE_mac->if_module = nr_ue_if_module_init(0)
Note right of main :            initFloatingCoresTpool(dlsch_threads, &nrUE_params.Tpool, false, "UE-tpool")
Note right of main :            NR_BCCH_BCH_Message_t *mib = get_new_MIB_NR(scc)
Note right of main :            nr_rrc_mac_config_req_mib(0, 0, mib->message.choice.mib, false)
Note right of main :            nr_rrc_mac_config_req_scg(0, 0, secondaryCellGroup)
Note right of main :            nr_ue_phy_config_request(&UE_mac->phy_config)
Note right of main :            initNamedTpool(gNBthreads, &gNB->threadPool, true, "gNB-tpool")
Note right of main :            initNotifiedFIFO(&gNB->L1_tx_free)
Note right of main :            initNotifiedFIFO(&gNB->L1_tx_filled)
Note right of main :            initNotifiedFIFO(&gNB->L1_tx_out)
Note right of main :            notifiedFIFO_elt_t *msgL1Tx = newNotifiedFIFO_elt(sizeof(processingData_L1tx_t),0,&gNB->L1_tx_free,processSlotTX)
Note right of main :            processingData_L1tx_t *msgDataTx = (processingData_L1tx_t *)NotifiedFifoData(msgL1Tx)
Note right of main :            init_DLSCH_struct(gNB, msgDataTx)
Note right of main :            int rx_size = (((14 * frame_parms->N_RB_DL * 12 * sizeof(int32_t)) + 15) >> 4) << 4
                                alt if (g_rbSize != 273)
                                end
Note right of main :            SNR = snr0
                                loop SNR < snr1
Note right of main :
Note right of main :            SNR += .2
                                end
                            )
Note right of main :            varArray_t *table_tx=initVarArray(1000,sizeof(double))
Note right of main :            reset_meas(&gNB->dlsch_scrambling_stats)
Note right of main :            reset_meas(&gNB->dlsch_interleaving_stats)
Note right of main :            reset_meas(&gNB->dlsch_rate_matching_stats)
Note right of main :            reset_meas(&gNB->dlsch_segmentation_stats)
Note right of main :            reset_meas(&gNB->dlsch_modulation_stats)
Note right of main :            reset_meas(&gNB->dlsch_encoding_stats)
Note right of main :            reset_meas(&gNB->tinput)
Note right of main :            reset_meas(&gNB->tprep)
Note right of main :            reset_meas(&gNB->tparity)
Note right of main :            reset_meas(&gNB->toutput)
                                alt if (n_trials== 1) num_rounds = 1
                                end
Note right of main :            trial = 0
                                loop trial < n_trials
Note right of main :
Note right of main :            trial++
                                end
                            )
                                alt if (Sched_INFO == NULL)
                                end
Note right of main :            exit(1)
                                loop while ((round<num_rounds) && (UE_harq_process->ack==0))
                                end
Note right of main :            clear_nr_nfapi_information(RC.nrmac[0], 0, frame, slot, &Sched_INFO->DL_req, &Sched_INFO->TX_req, &Sched_INFO->UL_dci_req)
Note right of main :            NR_SCHED_LOCK(&gNB_mac->sched_lock)
Note right of main :            nr_schedule_ue_spec(0, frame, slot, &Sched_INFO->DL_req, &Sched_INFO->TX_req)
Note right of main :            NR_SCHED_UNLOCK(&gNB_mac->sched_lock)
Note right of main :            pushNotifiedFIFO(&gNB->L1_tx_free,msgL1Tx)
Note right of main :            nr_schedule_response(Sched_INFO)
                                alt if(pdu_bit_map & 0x1)
                                end
Note right of main :            set_ptrs_symb_idx(&dlPtrsSymPos,
Note right of main :            ptrsSymbPerSlot = get_ptrs_symbols_in_slot(dlPtrsSymPos, pdsch_pdu_rel15->StartSymbolIndex, pdsch_pdu_rel15->NrOfSymbols)
                                alt if (run_initial_sync)
                                end
Note right of main :            nr_common_signal_procedures(gNB,frame,slot,msgDataTx->ssb[0].ssb_pdu)
Note right of main :            phy_procedures_gNB_TX(msgDataTx,frame,slot,1)
                                alt if (n_trials==1)
                                end
                                alt if (gNB->frame_parms.nb_antennas_tx>1)
                                end
Note right of main :            int tx_offset = frame_parms->get_samples_slot_timestamp(slot,frame_parms,0)
                                alt if (n_trials==1) printf("tx_offset %d, txdataF_offset %d \n", tx_offset,txdataF_offset)
                                end
Note right of main :            aa=0
                                loop aa<gNB->frame_parms.nb_antennas_tx
Note right of main :
Note right of main :            aa++
                                end
                            )
                                alt if (cyclic_prefix_type == 1)
                                end
Note right of main :            PHY_ofdm_mod((int *)&gNB->common_vars.txdataF[aa][txdataF_offset],
Note right of main :            nr_normal_prefix_mod(&gNB->common_vars.txdataF[aa][txdataF_offset],
                                alt if (n_trials==1)
                                end
Note right of main :            aa=0
                                loop aa<n_tx
Note right of main :
Note right of main :            aa++
                                end
                            )
                                alt if (output_fd)
                                end
Note right of main :            aa=0
                                loop aa<n_tx
Note right of main :
Note right of main :            aa++
                                end
                            )
Note right of main :            txlev[aa] = signal_energy((int32_t *)&txdata[aa][tx_offset+l_ofdm*frame_parms->ofdm_symbol_size + (l_ofdm-1)*frame_parms->nb_prefix_samples + frame_parms->nb_prefix_samples0],
                                alt if (n_trials==1) printf("txlev[%d] = %d (%f dB) txlev_sum %d\n",aa,txlev[aa],10*log10((double)txlev[aa]),txlev_sum)
                                end
Note right of main :            for (i=(frame_parms->get_samples_slot_timestamp(slot,frame_parms,0))
Note right of main :            i<(frame_parms->get_samples_slot_timestamp(slot+1,frame_parms,0))
Note right of main :            aa=0
                                loop aa<frame_parms->nb_antennas_tx
Note right of main :
Note right of main :            aa++
                                end
                            )
Note right of main :            sigma2_dB = 10 * log10((double)txlev_sum * ((double)UE->frame_parms.ofdm_symbol_size/(12*rel15->rbSize))) - SNR
Note right of main :            sigma2    = pow(10, sigma2_dB/10)
                                alt if (n_trials==1) printf("sigma2 %f (%f dB), txlev_sum %f (factor %f)\n",sigma2,sigma2_dB,10*log10((double)txlev_sum),(double)(double)UE->frame_parms.ofdm_symbol_size/(12*rel15->rbSize))
                                end
Note right of main :            aa=0
                                loop aa<n_rx
Note right of main :
Note right of main :            aa++
                                end
                            )
                                alt if (channel_model != AWGN) multipath_tv_channel(gNB2UE,
                                end
Note right of main :            for (i=frame_parms->get_samples_slot_timestamp(slot,frame_parms,0)
Note right of main :            i<frame_parms->get_samples_slot_timestamp(slot+1,frame_parms,0)
Note right of main :            int aa_rx=0
                                loop aa_rx<n_rx
Note right of main :
Note right of main :            aa_rx++
                                end
                            )
                                alt if (channel_model == AWGN)
                                end
Note right of main :            aa=0
                                loop aa<n_tx
Note right of main :
Note right of main :            aa++
                                end
                            )
Note right of main :            ((short*) UE->common_vars.rxdata[aa_rx])[2*i]   = (short) ((r_re[aa_rx][i] + sqrt(sigma2/2)*gaussdouble(0.0,1.0)))
Note right of main :            ((short*) UE->common_vars.rxdata[aa_rx])[2*i+1] = (short) ((r_im[aa_rx][i] + sqrt(sigma2/2)*gaussdouble(0.0,1.0)))
                                alt if (pdu_bit_map & 0x1)
                                end
Note right of main :            phase_noise(ts, &((short*) UE->common_vars.rxdata[aa_rx])[2*i],
Note right of main :            nr_ue_dcireq(&dcireq); //to be replaced with function pointer later
Note right of main :            nr_ue_scheduled_response(&scheduled_response)
Note right of main :            pbch_pdcch_processing(UE,
Note right of main :            pdsch_processing(UE,
                                alt if (dlsch0->last_iteration_cnt >= dlsch0->max_ldpc_iterations+1)
                                end
Note right of main :            uint16_t length_dmrs = get_num_dmrs(rel15->dlDmrsSymbPos)
Note right of main :            available_bits = nr_get_G(nb_rb, nb_symb_sch, nb_re_dmrs, length_dmrs, mod_order, rel15->nrOfLayers)
                                alt if (pdu_bit_map & 0x1)
                                end
                                alt if (trial == 0 && round == 0)
                                end
Note right of main :            i = 0
                                loop i < available_bits
Note right of main :
Note right of main :            i++
                                end
                            )
                                alt if(((gNB_dlsch->harq_process.f[i] == 0) && (UE_llr[i] <= 0)) ||
                                end
                                alt if (errors_scrambling[round] == 0)
                                end
Note right of main :            i = 0
                                loop i < TBS
Note right of main :
Note right of main :            i++
                                end
                            )
                                alt if (estimated_output_bit[i] != test_input_bit[i])
                                end
                                alt if(errors_bit == 0)
                                end
                                alt if (errors_bit > 0)
                                end
                                alt if (n_trials == 1)
                                end
                                alt if (UE_harq_process->ack==1) effRate += ((float)TBS)/round
                                end
Note right of main :            int r = 0
                                loop r < num_rounds
Note right of main :
Note right of main :            r++
                                end
                            )
Note right of main :            int r = 1
                                loop r < num_rounds
Note right of main :
Note right of main :            r++
                                end
                            )
Note right of main :            int r = 1
                                loop r < num_rounds
Note right of main :
Note right of main :            r++
                                end
                            )
Note right of main :            dump_pdsch_stats(stdout,gNB)
Note right of main :            int r = 1
                                loop r < num_rounds
Note right of main :
Note right of main :            r++
                                end
                            )
Note right of main :            int r = 1
                                loop r < num_rounds
Note right of main :
Note right of main :            r++
                                end
                            )
                                alt if (print_perf==1)
                                end
Note right of main :            printDistribution(&gNB->phy_proc_tx,table_tx,"PHY proc tx")
Note right of main :            printStatIndent2(&gNB->dlsch_encoding_stats,"DLSCH encoding time")
Note right of main :            printStatIndent3(&gNB->dlsch_segmentation_stats,"DLSCH segmentation time")
Note right of main :            printStatIndent3(&gNB->tinput,"DLSCH LDPC input processing time")
Note right of main :            printStatIndent3(&gNB->tprep,"DLSCH LDPC input preparation time")
Note right of main :            printStatIndent3(&gNB->tparity,"DLSCH LDPC parity generation time")
Note right of main :            printStatIndent3(&gNB->toutput,"DLSCH LDPC output generation time")
Note right of main :            printStatIndent3(&gNB->dlsch_rate_matching_stats,"DLSCH Rate Mataching time")
Note right of main :            printStatIndent3(&gNB->dlsch_interleaving_stats,  "DLSCH Interleaving time")
Note right of main :            printStatIndent2(&gNB->dlsch_modulation_stats,"DLSCH modulation time")
Note right of main :            printStatIndent2(&gNB->dlsch_scrambling_stats,  "DLSCH scrambling time")
Note right of main :            printStatIndent2(&gNB->dlsch_layer_mapping_stats, "DLSCH Layer Mapping time")
Note right of main :            printStatIndent2(&gNB->dlsch_resource_mapping_stats, "DLSCH Resource Mapping time")
Note right of main :            printStatIndent2(&gNB->dlsch_precoding_stats,"DLSCH Layer Precoding time")
Note right of main :            printDistribution(&phy_proc_rx_tot, table_rx,"Total PHY proc rx")
Note right of main :            printStatIndent(&ue_front_end_tot,"Front end processing")
Note right of main :            printStatIndent(&dlsch_llr_tot,"rx_pdsch processing")
Note right of main :            printStatIndent2(&pdsch_procedures_tot,"pdsch processing")
Note right of main :            printStatIndent2(&dlsch_procedures_tot,"dlsch processing")
Note right of main :            printStatIndent2(&UE->crnti_procedures_stats,"C-RNTI processing")
Note right of main :            printStatIndent(&UE->ofdm_demod_stats,"ofdm demodulation")
Note right of main :            printStatIndent(&UE->dlsch_channel_estimation_stats,"DLSCH channel estimation time")
Note right of main :            printStatIndent(&UE->dlsch_freq_offset_estimation_stats,"DLSCH frequency offset estimation time")
Note right of main :            printStatIndent(&dlsch_decoding_tot, "DLSCH Decoding time ")
Note right of main :            printStatIndent(&UE->dlsch_unscrambling_stats,"DLSCH unscrambling time")
Note right of main :            printStatIndent(&UE->dlsch_rate_unmatching_stats,"DLSCH Rate Unmatching")
Note right of main :            printStatIndent2(&UE->dlsch_tc_init_stats,"init")
Note right of main :            printStatIndent2(&UE->dlsch_tc_alpha_stats,"alpha")
Note right of main :            printStatIndent2(&UE->dlsch_tc_beta_stats,"beta")
Note right of main :            printStatIndent2(&UE->dlsch_tc_gamma_stats,"gamma")
Note right of main :            printStatIndent2(&UE->dlsch_tc_ext_stats,"ext")
Note right of main :            printStatIndent2(&UE->dlsch_tc_intl1_stats,"turbo internal interleaver")
Note right of main :            printStatIndent2(&UE->dlsch_tc_intl2_stats,"intl2+HardDecode+CRC")
                                alt if (n_trials == 1)
                                end
                                alt if (UE->frame_parms.nb_antennas_rx>1)
                                end
Note right of main :            write_output("rxF_comp.m","rxFc",UE->phy_sim_pdsch_rxdataF_comp,N_RB_DL*12*14,1,1)
                                alt if (effRate > (eff_tp_check*TBS))
                                end
Note right of main :            free_channel_desc_scm(gNB2UE)
Note right of main :            i = 0
                                loop i < n_tx
Note right of main :
Note right of main :            i++
                                end
                            )
Note right of main :            i = 0
                                loop i < n_rx
Note right of main :
Note right of main :            i++
                                end
                            )
                                alt if (output_fd)
                                end
Note right of main :            fclose(output_fd)
                                alt if (input_fd)
                                end
Note right of main :            fclose(input_fd)
                                alt if (scg_fd)
                                end
Note right of main :            fclose(scg_fd)
Note right of main :            void update_ptrs_config(NR_CellGroupConfig_t *secondaryCellGroup, uint16_t *rbSize, uint8_t *mcsIndex, int8_t *ptrs_arg)
                                alt if(ptrs_arg[0] ==0)
                                else if(ptrs_arg[0] == 1)
                                else if(ptrs_arg[0] ==2)
                                end
                                alt if(ptrs_arg[1] ==2)
                                else if(ptrs_arg[1] == 4)
                                end
Note right of main :            rrc_config_dl_ptrs_params(bwp, ptrsFreqDenst, ptrsTimeDenst, &epre_Ratio, &reOffset)
Note right of main :            void update_dmrs_config(NR_CellGroupConfig_t *scg, int8_t* dmrs_arg)
                                alt if(dmrs_arg[0] == 0)
                                else if (dmrs_arg[0] == 1)
                                end
                                alt if(dmrs_arg[1] >= 0 && dmrs_arg[1] <4 )
                                end
                                alt if(dmrs_arg[2] == 1)
                                end
Note right of main :            } else if(dmrs_arg[2] == 2)
                                alt if(mapping_type == typeA)
                                end
                                alt if (dmrs_config_type == NFAPI_NR_DMRS_TYPE2)
                                end
                                alt if(mapping_type == typeB)
                                end
                                alt if (dmrs_config_type == NFAPI_NR_DMRS_TYPE2)
                                end
                                alt if (add_pos != 2) { // pos0,pos1,pos3
                                end
                                alt if (dmrs_config->dmrs_AdditionalPosition == NULL)
                                end
Note right of main :            int i=0
                                loop i<bwp->bwp_Common->pdsch_ConfigCommon->choice.setup->pdsch_TimeDomainAllocationList->list.count
Note right of main :
Note right of main :            i++
                                end
                            )

```
