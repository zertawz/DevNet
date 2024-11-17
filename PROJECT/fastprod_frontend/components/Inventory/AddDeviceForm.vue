<template>
  <div>
    <ValidationObserver
      ref="observer"
      v-slot="{ handleSubmit, validated, invalid }"
    >
      <v-form @submit.prevent="onSubmit">
        <v-row>
          <v-col lg="6" md="6" cols="12">
            <ValidationProvider
              v-slot="{ errors, valid }"
              rules="required"
              name="Hostname"
            >
              <v-text-field
                v-model="host.data.device_name"
                :error-messages="errors"
                color="primary"
                outlined
                label="Hostname"
                prepend-inner-icon="mdi-subtitles-outline"
              ></v-text-field>
            </ValidationProvider>
          </v-col>
          <v-col lg="6" md="6" cols="12">
            <ValidationProvider
              v-slot="{ errors, valid }"
              rules="required"
              name="Ip address"
            >
              <v-text-field
                v-model="host.hostname"
                :error-messages="errors"
                color="primary"
                outlined
                label="Ip address"
                prepend-inner-icon="mdi-router-network"
              ></v-text-field>
            </ValidationProvider>
          </v-col>

          <v-col lg="6" md="6" cols="12">
            <ValidationProvider
              v-slot="{ errors, valid }"
              rules="required"
              name="Model"
            >
              <v-text-field
                v-model="host.data.device_model"
                :error-messages="errors"
                color="primary"
                outlined
                label="Model"
                prepend-inner-icon="mdi-cog-sync-outline"
              ></v-text-field>
            </ValidationProvider>
          </v-col>
          <v-col lg="6" md="6" cols="12">
            <ValidationProvider
              v-slot="{ errors, valid }"
              rules="required"
              name="Type"
            >
              <v-select
                v-model="host.data.device_type"
                :items="['router', 'routeur_switch']"
                outlined
                :error-messages="errors"
                color="primary"
                label="Type"
                prepend-inner-icon="mdi-devices"
              ></v-select>
            </ValidationProvider>
          </v-col>
          <v-col lg="6" md="6" cols="12">
            <ValidationProvider
              v-slot="{ errors, valid }"
              rules="required"
              name="Locality"
            >
              <v-text-field
                v-model="host.data.locality"
                :error-messages="errors"
                color="primary"
                outlined
                label="Locality"
                prepend-inner-icon="mdi-map-marker-radius-outline"
              ></v-text-field>
            </ValidationProvider>
          </v-col>
          <v-col lg="6" md="6" cols="12">
            <ValidationProvider
              v-slot="{ errors, valid }"
              rules="required"
              name="Building"
            >
              <v-text-field
                v-model="host.data.building"
                :error-messages="errors"
                color="primary"
                outlined
                label="Building"
                prepend-inner-icon="mdi-office-building-marker-outline"
              ></v-text-field>
            </ValidationProvider>
          </v-col>
          <v-col lg="8" md="8" cols="12">
            <ValidationProvider
              v-slot="{ errors, valid }"
              rules="required"
              name="Room"
            >
              <v-text-field
                v-model="host.data.room"
                :error-messages="errors"
                color="primary"
                outlined
                label="Room"
                prepend-inner-icon="mdi-domain"
              ></v-text-field>
            </ValidationProvider>
          </v-col>
        </v-row>
        <div class="text-center">
          <v-btn
            :disabled="invalid"
            color="primary"
            class="white--text"
            x-large
            :loading="loading"
            @click="add"
            outlined
          >
            Add <v-icon right dark> mdi-check </v-icon>
          </v-btn>
        </div>
      </v-form>
    </ValidationObserver>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      host: {
        hostname: null,
        data: {
          device_type: null,
          device_name: null,
          device_model: null,
          locality: "cisco",
          building: null,
          room: null,
        },
      },
    };
  },

  mounted() {},
  methods: {
    add() {
      this.loading = true;
      this.$store
        .dispatch("inventory/post", { data: this.host })
        .then((response) => {
          this.loading = false;
          this.$emit("onSubmit");
        })
        .catch((error) => {
          this.loading = false;
          console.log("error", error);
        });
    },
  },
};
</script>
<style scoped></style>
