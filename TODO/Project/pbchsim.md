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
```

##### 参数说明
`./nr_pbchsim -F input_filename -g channel_mod -h(elp) -I(nitial sync) -L log_lvl -n n_frames -M SSBs -n frames -N cell_id -o FO -P phase -r seed -R RBs -s snr0 -S snr1 -x transmission_mode -y TXant -z RXant`
| 参数 |                                                                                                                  | 说明                                                                                                                 |
| ---- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| -F   | -F RX一致性测试的输入文件名（.txt格式）                                                                          | Input filename (.txt format) for RX conformance testing                                                              |
| -g   | -g[A，B，C，D，E，F，g]使用3GPP SCM（A、B、C、D）或36-101（E-EPA、F-EVA、g-ETU）模型（忽略延迟扩展和Ricean因子） | [A,B,C,D,E,F,G] Use 3GPP SCM (A,B,C,D) or 36-101 (E-EPA,F-EVA,G-ETU) models (ignores delay spread and Ricean factor) |
| -h   | -h此消息                                                                                                         | This message                                                                                                         |
| -I   | -我运行初始同步，目标错误率为0.1                                                                                 | run initial sync with target error rate 0.1                                                                          |
| -L   | -L设置日志级别（-1禁用，0错误，1警告，2信息，3调试，4跟踪）                                                      | set the log level (-1 disable, 0 error, 1 warning, 2 info, 3 debug, 4 trace)                                         |
| -m   | -m数字索引                                                                                                       | Numerology index                                                                                                     |
| -M   | -M突发中的多个SSB位置                                                                                            | Multiple SSB positions in burst                                                                                      |
| -n   | -n要模拟的帧数                                                                                                   | Number of frames to simulate                                                                                         |
| -N   | -N镍氢电池                                                                                                       | Nid_cell                                                                                                             |
| -o   | -o载波频率偏移（Hz）                                                                                             | Carrier frequency offset in Hz                                                                                       |
| -O   | -O SSB子载波偏移                                                                                                 | SSB subcarrier offset                                                                                                |
| -P   | -P PBCH相位，允许值0-3                                                                                           | PBCH phase, allowed values 0-3                                                                                       |
| -r   | -r设置随机数生成器种子（默认值：0=当前时间）                                                                     | set the random number generator seed (default: 0 = current time)                                                     |
| -R   | -R N_RB_DL                                                                                                       | N_RB_DL                                                                                                              |
| -s   | -s起始SNR，从SNR0运行到SNR0+10 dB（如果未给出-s）。如果-n 1，则仅模拟SNR                                         | Starting SNR, runs from SNR0 to SNR0 + 10 dB if not -S given. If -n 1, then just SNR is simulated                    |
| -S   | -S结束SNR，从SNR0运行到SNR1                                                                                      | Ending SNR, runs from SNR0 to SNR1                                                                                   |
| -x   | -x传输模式（目前为1,2,6）                                                                                        | Transmission mode (1,2,6 for the moment)                                                                             |
| -y   | -y eNB中使用的TX天线数量                                                                                         | Number of TX antennas used in eNB                                                                                    |
| -z   | -z UE中使用的RX天线数量                                                                                          | Number of RX antennas used in UE                                                                                     |

##### 代码解析
* main
```mermaid
  sequenceDiagram
    Note right of main      : int main(int argc, char **argv)
    Note right of main      : get_softmodem_params()->sa = 1
    Note right of main      : __attribute__((unused))
    Note right of main      : cpuf = get_cpu_freq_GHz()
    alt if ( load_configmodule(argc,argv,CONFIG_ENABLECMDLINEONLY) == 0)
    end
    Note right of main      : exit_fun("[NR_PBCHSIM] Error, configuration module init failed\n")
    loop while ((c = getopt (argc, argv, "F:g:hIL:m:M:n:N:o:O:P:r:R:s:S:x:y:z:")) != -1)
    end
    Note right of main      : switch (c)
    Note right of main      : output_fd = fopen(optarg,"w")
    alt if (output_fd==NULL)
    end
    Note right of main      : exit(-1)
    Note right of main      : input_fd = fopen(optarg,"r")
    alt if (input_fd==NULL)
    end
    Note right of main      : exit(-1)
    Note right of main      : switch((char)*optarg)
    Note right of main      : exit(-1)
    alt if (pbch_phase>3)
    end
    Note right of main      : ricean_factor = pow(10,-.1*atof(optarg))
    alt if (ricean_factor>1)
    end
    Note right of main      : exit(-1)
    alt if ((transmission_mode!=1) && (transmission_mode!=2) && (transmission_mode!=6))
    end
    Note right of main      : exit(-1)
    alt if ((n_tx==0) || (n_tx>2))
    end
    Note right of main      : exit(-1)
    alt if ((n_rx==0) || (n_rx>2))
    end
    Note right of main      : exit(-1)
    Note right of main      : exit (-1)
    Note right of main      : randominit(seed)
    Note right of main      : logInit()
    Note right of main      : set_glog(loglvl)
    alt if (snr1set==0)
    end
    Note right of main      : nr_phy_config_request_sim_pbchsim(gNB,N_RB_DL,N_RB_DL,mu,Nid_cell,SSB_positions)
    Note right of main      : set_tdd_config_nr(&gNB->gNB_config, mu, 7, 6, 2, 4)
    Note right of main      : phy_init_nr_gNB(gNB)
    Note right of main      : switch (mu)
    alt if (N_RB_DL == 217)
    else if (N_RB_DL == 245)
    else if (N_RB_DL == 273)
    else if (N_RB_DL == 106)
    end
    Note right of main      : else AssertFatal(1==0,"Unsupported numerology for mu %d, N_RB %d\n",mu, N_RB_DL)
    alt if (N_RB_DL == 66)
    end
    Note right of main      : else AssertFatal(1==0,"Unsupported numerology for mu %d, N_RB %d\n",mu, N_RB_DL)
    alt if(eps!=0.0)
    end
    alt if (eps>0)
    end
    Note right of main      : gNB2UE = new_channel_desc_scm(n_tx,
    alt if (gNB2UE==NULL)
    end
    Note right of main      : exit(-1)
    Note right of main      : i=0
    loop  i<2
      Note right of main      : 
      Note right of main      : i++
    end
)
    alt if (pbch_file_fd!=NULL)
    end
    Note right of main      : load_pbch_desc(pbch_file_fd)
    alt if (run_initial_sync==1)  UE->is_synchronized = 0
    end
    alt if(eps!=0.0)
    end
    alt if (init_nr_ue_signal(UE, 1) != 0)
    end
    Note right of main      : exit(-1)
    Note right of main      : nr_gold_pbch(UE)
    Note right of main      : __attribute__ ((aligned(32))) c16_t rxdataF[UE->frame_parms.nb_antennas_rx][rxdataF_sz]
    alt if (input_fd==NULL)
    end
    Note right of main      : i=0
    loop  i<frame_parms->Lmax
      Note right of main      : 
      Note right of main      : i++
    end
)
    alt if((SSB_positions >> i) & 0x01)
    end
    Note right of main      : start_symbol = nr_get_ssb_start_symbol(frame_parms,i)
    Note right of main      : aa=0
    loop  aa<gNB->frame_parms.nb_antennas_tx
      Note right of main      : 
      Note right of main      : aa++
    end
)
    Note right of main      : nr_common_signal_procedures (gNB,frame,slot,msgDataTx.ssb[i].ssb_pdu)
    Note right of main      : aa=0
    loop  aa<gNB->frame_parms.nb_antennas_tx
      Note right of main      : 
      Note right of main      : aa++
    end
)
    alt if (cyclic_prefix_type == 1)
    end
    Note right of main      : apply_nr_rotation(frame_parms,
    Note right of main      : PHY_ofdm_mod((int *)gNB->common_vars.txdataF[aa],
    Note right of main      : &txdata[aa][frame_parms->get_samples_slot_timestamp(slot,frame_parms,0)],
    Note right of main      : apply_nr_rotation(frame_parms,
    Note right of main      : &txdata[aa][frame_parms->get_samples_slot_timestamp(slot,frame_parms,0)],
    Note right of main      : PHY_ofdm_mod((int *)gNB->common_vars.txdataF[aa],
    Note right of main      : (int*)&txdata[aa][frame_parms->get_samples_slot_timestamp(slot,frame_parms,0)],
    Note right of main      : PHY_ofdm_mod((int *)&gNB->common_vars.txdataF[aa][frame_parms->ofdm_symbol_size],
    Note right of main      : (int*)&txdata[aa][frame_parms->get_samples_slot_timestamp(slot,frame_parms,0)+frame_parms->nb_prefix_samples0+frame_parms->ofdm_symbol_size],
    alt if (gNB->frame_parms.nb_antennas_tx>1)
    end
    alt if (fread(txdata[0],
    end
    alt if (gNB->frame_parms.nb_antennas_tx>1)
    end
    alt if (output_fd) 
    end
    Note right of main      : SNR=snr0
    loop  SNR<snr1
      Note right of main      : 
      Note right of main      : SNR+=.2
    end
)
    Note right of main      : trial=0
    loop  trial<n_trials
      Note right of main      : 
      Note right of main      : trial++
    end
)
    Note right of main      : i=0
    loop  i<frame_length_complex_samples
      Note right of main      : 
      Note right of main      : i++
    end
)
    Note right of main      : aa=0
    loop  aa<frame_parms->nb_antennas_tx
      Note right of main      : 
      Note right of main      : aa++
    end
)
    Note right of main      : sigma2_dB = 20*log10((double)AMP/4)-SNR
    Note right of main      : sigma2 = pow(10,sigma2_dB/10)
    alt if(eps!=0.0)
    end
    Note right of main      : rf_rx(r_re,  // real part of txdata
    Note right of main      : 0.0); // IQ phase imbalance (rad)
    Note right of main      : i=0
    loop  i<frame_length_complex_samples
      Note right of main      : 
      Note right of main      : i++
    end
)
    Note right of main      : aa=0
    loop  aa<frame_parms->nb_antennas_rx
      Note right of main      : 
      Note right of main      : aa++
    end
)
    Note right of main      : ((short*) UE->common_vars.rxdata[aa])[2*i]   = (short) ((r_re[aa][i] + sqrt(sigma2/2)*gaussdouble(0.0,1.0)))
    Note right of main      : ((short*) UE->common_vars.rxdata[aa])[2*i+1] = (short) ((r_im[aa][i] + sqrt(sigma2/2)*gaussdouble(0.0,1.0)))
    alt if (n_trials==1)
    end
    alt if (gNB->frame_parms.nb_antennas_tx>1)
    end
    alt if (UE->is_synchronized == 0)
    end
    Note right of main      : ret = nr_initial_sync(&proc, UE, 1, 0)
    alt if (ret<0) n_errors++
    end
    Note right of main      : __attribute__((aligned(32))) struct complex16 dl_ch_estimates[frame_parms->nb_antennas_rx][estimateSz]
    Note right of main      : __attribute__((aligned(32))) struct complex16 dl_ch_estimates_time[frame_parms->nb_antennas_rx][frame_parms->ofdm_symbol_size]
    loop while (!((SSB_positions >> ssb_index) & 0x01))
    end
    Note right of main      : UE->symbol_offset = nr_get_ssb_start_symbol(frame_parms, ssb_index)
    Note right of main      : int i=UE->symbol_offset+1
    loop  i<UE->symbol_offset+4
      Note right of main      : 
      Note right of main      : i++
    end
)
    Note right of main      : nr_slot_fep(UE,
    Note right of main      : nr_pbch_channel_estimation(UE,estimateSz, dl_ch_estimates, dl_ch_estimates_time, &proc, 
    Note right of main      : ret = nr_rx_pbch(UE,
    alt if (ret==0)
    end
    Note right of main      : int i=0
    loop  i<8
      Note right of main      : 
      Note right of main      : i++
    end
)
    Note right of main      : i=0
    loop i<3
      Note right of main      : 
      Note right of main      : i++
    end
)
    alt if (payload_ret!=4) 
    end
    alt if (ret!=0) n_errors++
    end
    alt if (((float)n_errors/(float)n_trials <= target_error_rate) && (n_errors_payload==0))
    end
    alt if (n_trials==1)
    end
    Note right of main      : free_channel_desc_scm(gNB2UE)
    Note right of main      : int i = 0
    loop  i < nb_slots_to_set
      Note right of main      : 
      Note right of main      : ++i
    end
)
    Note right of main      : phy_free_nr_gNB(gNB)
    Note right of main      : term_nr_ue_signal(UE, 1)
    Note right of main      : i=0
    loop  i<2
      Note right of main      : 
      Note right of main      : i++
    end
)
    alt if (output_fd)
    end
    Note right of main      : fclose(output_fd)
    alt if (input_fd)
    end
    Note right of main      : fclose(input_fd)
    Note right of main      : loader_reset()
    Note right of main      : logTerm()
    Note right of main      : return(n_errors)
```
